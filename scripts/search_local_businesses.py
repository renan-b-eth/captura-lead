"""
Busca georreferenciada de comércios locais utilizando o treg CLI e Serper Google Maps API.
Local de referência: E.E. Professora Nancy de Oliveira Fidalgo (São Paulo - SP)
"""
import subprocess
import json
import math

SCHOOL_LAT = -23.5257503
SCHOOL_LON = -46.4244228

def haversine(lat1, lon1, lat2, lon2):
    R = 6371000  # Raio em metros
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)
    a = math.sin(delta_phi / 2.0) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2.0) ** 2
    return R * (2 * math.atan2(math.sqrt(a), math.sqrt(1 - a)))

categories = [
    ("Mercados e Mercearias", "mercado"),
    ("Padarias e Confeitarias", "padaria"),
    ("Farmácias e Drogarias", "farmacia"),
    ("Restaurantes e Lanchonetes", "restaurante"),
    ("Pizzarias e Lanches", "pizzaria"),
    ("Lojas e Serviços", "loja")
]

all_places = {}

for cat_name, query in categories:
    payload = {
        "q": query,
        "ll": f"@{SCHOOL_LAT},{SCHOOL_LON},16z",
        "hl": "pt-br"
    }
    with open("temp_query.json", "w", encoding="utf-8") as f:
        json.dump(payload, f)
        
    cmd = ["treg", "call", "serper.google.serp.maps", "--method", "POST", "--file", "temp_query.json", "--json"]
    try:
        res = subprocess.run(cmd, capture_output=True, text=False)
        raw_output = res.stdout.decode("utf-8", errors="replace")
        data = json.loads(raw_output)
        places = data.get("result", {}).get("places", [])
        
        for p in places:
            if p.get("latitude") and p.get("longitude"):
                p["distance_meters"] = round(haversine(SCHOOL_LAT, SCHOOL_LON, p["latitude"], p["longitude"]))
                
        places.sort(key=lambda x: x.get("distance_meters", 999999))
        all_places[cat_name] = places
        print(f"Sucesso: {len(places)} estabelecimentos em '{cat_name}'")
    except Exception as e:
        print(f"Erro em {cat_name}: {e}")

with open("data/comercios_locais_sp.json", "w", encoding="utf-8") as f:
    json.dump(all_places, f, ensure_ascii=False, indent=2)

print("Finalizado! Dados salvos em data/comercios_locais_sp.json")
