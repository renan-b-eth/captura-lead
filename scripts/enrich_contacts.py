"""
Enriquecimento de contatos, links diretos de WhatsApp e busca de e-mails institucionais
utilizando o treg CLI e Crawl4ai Google Organic SERP API.
"""
import subprocess
import json
import re

email_regex = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
phone_clean = re.compile(r'\D')

def enrich_establishment(name, phone, address):
    whatsapp = None
    if phone:
        digits = phone_clean.sub('', phone)
        if '119' in digits or (len(digits) == 11 and digits.startswith('119')):
            if not digits.startswith('55'):
                digits = '55' + digits
            whatsapp = f"https://wa.me/{digits}"
        else:
            whatsapp = f"{phone} (Telefone Fixo Comercial)"
            
    payload = {
        "q": f'"{name}" "São Paulo" (email OR whatsapp OR "@" OR "contato" OR "cnpj")',
        "country": "br",
        "language": "pt",
        "limit": 5
    }
    with open("temp_enrich.json", "w", encoding="utf-8") as f:
        json.dump(payload, f)
        
    cmd = ["treg", "call", "treg.google.serp.organic", "--method", "POST", "--file", "temp_enrich.json", "--json"]
    
    found_emails = set()
    found_links = []
    
    try:
        res = subprocess.run(cmd, capture_output=True, text=False)
        raw = res.stdout.decode('utf-8', errors='replace')
        data = json.loads(raw)
        results = data.get("result", {}).get("output", {}).get("results", [])
        if not results:
            results = data.get("result", {}).get("raw", {}).get("results", [])
            
        for r in results:
            snippet = r.get("snippet", "") + " " + r.get("title", "")
            url = r.get("url", "")
            
            matches = email_regex.findall(snippet)
            for m in matches:
                clean_m = m.strip('.').lower()
                if not any(clean_m.endswith(ext) for ext in ['.png', '.jpg', '.jpeg', '.webp']):
                    found_emails.add(clean_m)
                    
            if any(k in url or k in snippet.lower() for k in ['wa.me', 'instagram.com', 'facebook.com']):
                found_links.append(url)
    except Exception as e:
        print(f"Erro ao enriquecer {name}: {e}")
        
    return {
        "name": name,
        "phone": phone,
        "whatsapp": whatsapp,
        "emails": list(found_emails),
        "links": found_links[:3]
    }

if __name__ == "__main__":
    print("Módulo de enriquecimento de contatos via Treg.")
