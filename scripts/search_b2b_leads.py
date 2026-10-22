"""
Busca de leads B2B (CTOs, CPTOs, VPs e Heads de Engenharia) na capital de São Paulo
para consultoria de Claude Code utilizando o treg CLI e QuickEnrich People Search API.
"""
import subprocess
import json

targets = [
    {
        "category": "Fábricas de Software e Consultorias Dev",
        "filter": {
            "title": {"include": ["CTO", "Head of Engineering", "Chief Technology Officer", "Diretor de Tecnologia"], "exclude": ["Sales", "HR", "Marketing"]},
            "city": {"include": ["São Paulo"], "exclude": []},
            "country_code": {"include": ["BR"], "exclude": []},
            "industry_linkedin": {"include": ["Software Development", "IT Services and IT Consulting"], "exclude": []},
            "per_page": 15
        }
    },
    {
        "category": "Startups e Scaleups Tech / SaaS",
        "filter": {
            "title": {"include": ["CTO", "Head of Engineering", "VP of Engineering"], "exclude": ["Sales", "HR", "Marketing"]},
            "city": {"include": ["São Paulo"], "exclude": []},
            "country_code": {"include": ["BR"], "exclude": []},
            "number_of_employees": {"include": ["20 - 99", "100 - 249", "250 - 499", "500 - 999"], "exclude": []},
            "per_page": 15
        }
    }
]

all_leads = {}

for target in targets:
    cat = target["category"]
    with open("temp_query_lead.json", "w", encoding="utf-8") as f:
        json.dump(target["filter"], f)
        
    cmd = ["treg", "call", "quickenrich.people.search", "--method", "POST", "--file", "temp_query_lead.json", "--json"]
    try:
        res = subprocess.run(cmd, capture_output=True, text=False)
        raw = res.stdout.decode("utf-8", errors="replace")
        data = json.loads(raw)
        items = data.get("result", {}).get("data", [])
        all_leads[cat] = items
        print(f"Sucesso: {len(items)} leads encontrados para '{cat}'")
    except Exception as e:
        print(f"Erro em {cat}: {e}")

with open("data/leads_consultoria_claude.json", "w", encoding="utf-8") as f:
    json.dump(all_leads, f, ensure_ascii=False, indent=2)

print("Finalizado! Dados salvos em data/leads_consultoria_claude.json")
