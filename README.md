# 🎯 Captura e Enriquecimento de Leads com Treg & IA

Repositório de automação e dados para **prospecção e enriquecimento de leads (B2B e Local)** na capital de São Paulo, utilizando o **[treg](https://github.com/superdesigndev/treg)** como hub unificado de ferramentas para agentes de IA e APIs de dados (Google Maps, Google SERP, Apollo e QuickEnrich).

---

## 📁 Estrutura do Repositório

```text
├── data/
│   ├── comercios_locais_sp.json          # 115 comércios locais mapeados e categorizados
│   ├── contatos_enriquecidos.json        # Telefones, WhatsApps e e-mails enriquecidos
│   └── leads_consultoria_claude.json     # 30 leads B2B de CTOs e Heads de TI em SP
├── reports/
│   ├── comercios_ee_nancy.md             # Relatório de comércios próximos à E.E. Nancy de Oliveira Fidalgo
│   ├── contatos_comercios_nancy.md       # Tabela de contatos com links diretos para WhatsApp (wa.me)
│   └── leads_consultoria_claude.md       # Relatório executivo de prospecção para consultoria Claude Code
├── scripts/
│   ├── search_local_businesses.py        # Script de busca georreferenciada via Treg (Google Maps / Serper)
│   ├── enrich_contacts.py                # Script de enriquecimento de contatos, WhatsApp e e-mails
│   └── search_b2b_leads.py               # Script de busca de tomadores de decisão B2B em SP
├── .gitignore                            # Filtro de arquivos temporários e caches
└── README.md                             # Documentação completa do projeto
```

---

## 🛠️ Tecnologias e Ferramentas Utilizadas

- **Python 3.13**
- **[treg CLI](https://github.com/superdesigndev/treg)** (`tools-registry` v0.27.0): Roteamento unificado de ferramentas para agentes e injeção server-side de credenciais.
- **Provedores de Dados Integrados pelo Treg:**
  - `serper.google.serp.maps`: Busca precisa de estabelecimentos por coordenadas geográficas e zoom.
  - `crawl4ai.google.serp.organic`: Varredura em tempo real para descoberta de e-mails, CNPJs e links de WhatsApp.
  - `quickenrich.people.search`: Descoberta B2B de tomadores de decisão (CTOs, CPTOs, VPs de Engenharia) com links de LinkedIn e dados de empresa.
  - `apollo.people.search`: Base de dados de profissionais e executivos.

---

## 📍 1. Mapeamento Local: E.E. Professora Nancy de Oliveira Fidalgo (SP)

- **Referência:** Rua Miguel Arcanjo Dutra, 253 - Jardim Santa Terezinha / Guaianases, São Paulo - SP (`-23.5257503, -46.4244228`).
- **Escopo:** Mapeamento de 115 estabelecimentos divididos em 6 categorias essenciais (Pizzarias, Mercados, Restaurantes, Padarias, Farmácias e Lojas).
- **Resultados:**
  - Cálculo de distância métrica exata de cada comércio até a escola via fórmula de Haversine.
  - Enriquecimento com links diretos de WhatsApp (`https://wa.me/55...`) e identificação de telefones fixos e e-mails corporativos.
  - Relatório completo disponível em [`reports/contatos_comercios_nancy.md`](reports/contatos_comercios_nancy.md).

---

## 🚀 2. Prospecção B2B: Consultoria de Claude Code em São Paulo

Mapeamento de decisores de tecnologia na capital de São Paulo para serviços de consultoria, implantação e treinamento em **Claude Code** (agente autônomo de terminal da Anthropic).

### Segmentação de Alvos
1. **Fábricas de Software & Consultorias Dev (Dev Shops):** Empresas que faturam por hora/projeto e cujo ganho de produtividade com Claude Code gera expansão imediata de margem operacional.
   - *Exemplos:* **Abaccus Software**, **nstech**, **SampleMed**, **Valemobi**, **Better Now**, **GD Solutions**.
2. **Startups & Scaleups de Tecnologia (SaaS & Fintechs):** Times com alta pressão de entrega e débitos técnicos acumulados.
   - *Exemplos:* **Clicksign**, **CRM&BÔNUS**, **Zippi**, **InfoPrice**, **CUBi Energia**, **NeuralMed**.

A lista completa com perfis de LinkedIn, portes de empresa e templates de abordagem fria está em [`reports/leads_consultoria_claude.md`](reports/leads_consultoria_claude.md).

---

## 💰 Transparência de Custos (Treg Ledger)

Todas as requisições foram orquestradas com custo mínimo diretamente pelo ledger do `treg`:

* **Saldo Inicial:** `$1.0000 USD` *(Crédito promocional de boas-vindas)*
* **Saldo Restante:** **`$0.9419 USD`**
* **Custo Total Consumido:** **`$0.0581 USD`** (~**R$ 0,33** na cotação atual)
* **Custo Médio por Lead:** Menos de **R$ 0,014** por lead completamente enriquecido.

---

## ⚙️ Como Executar os Scripts

### Pré-requisitos
1. Ter o Python 3.12 ou 3.13 instalado.
2. Instalar o CLI do treg:
   ```bash
   pip install "tools-registry[proxy]"
   ```
3. Autenticar sua chave:
   ```bash
   treg config --base-url https://treg.to
   treg login --token <SEU_TOKEN_TREG>
   ```

### Executando as automações
```bash
# 1. Buscar comércios locais no entorno da escola
python scripts/search_local_businesses.py

# 2. Buscar tomadores de decisão B2B em São Paulo
python scripts/search_b2b_leads.py
```

---
*Projeto mantido por [renan-b-eth](https://github.com/renan-b-eth).*
