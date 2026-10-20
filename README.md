<h1 align="center">🪙 WoW Market Arbitrage Agent 🪙</h1>

<p align="center">
<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=22&pause=1000&color=0070F3&center=true&vCenter=true&width=700&lines=Real-Time+Auction+ETL+Pipeline;PostgreSQL+Time-Series+Analytics;Quantitative+Market+Arbitrage;Powered+by+Blizzard+OAuth2+%2B+Gemini" />
</p>

<p align="center">
<img src="https://img.shields.io/badge/Python-3.10+-111111?style=for-the-badge"/>
<img src="https://img.shields.io/badge/PostgreSQL-15-0070F3?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Docker-Containers-111111?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Google-Gemini_LLM-0070F3?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Discord-Webhooks-111111?style=for-the-badge"/>
</p>

---

## Overview

Pipeline automatizado de ingestão de dados, modelagem relacional e detecção de arbitragem financeira na Casa de Leilões (Auction House) do World of Warcraft.

O sistema monitora mais de 280.000 lotes ativos de commodities em escala regional através da API oficial da Blizzard, persiste snapshots históricos no PostgreSQL, calcula desvios estatísticos de preço e utiliza LLM (Google Gemini) para gerar alertas executivos acionáveis via Discord.

---

## Exemplo de Output gerado.
<img width="1308" height="487" alt="{462A1311-D2A7-4A22-8BB3-59E1F941E16B}" src="https://github.com/user-attachments/assets/17f57b97-474a-4b01-9fa5-86c9f092b4f2" />

---

## Capabilities

- autenticação segura OAuth2 com a infraestrutura oficial da Blizzard  
- processamento e filtragem de grandes volumes de leilões ativos (~300k itens) em tempo real  
- normalização monetária automática (conversão de copper para gold)  
- modelagem relacional com persistência de time-series snapshots  
- cálculo analítico de desvio de preço e média ponderada via SQL  
- análise qualitativa de risco/recompensa e contexto de expansão com IA  
- entrega automatizada de alertas de compra/venda direto em webhook do Discord  

---

## Stack

- Python 3.10+ (`psycopg2-binary`, `requests`, `google-genai`, `python-dotenv`)  
- PostgreSQL 15 (Docker)  
- Blizzard Battle.net OAuth2 REST API  
- Google Gemini API (`gemini-2.5-flash`)  
- Discord Webhooks  
- DBeaver (SQL Administration)  

---

## Core Features

- **Ingestão em Larga Escala:** extrai dumps completos de commodities regionais da Blizzard  
- **Modelagem Relacional Normalizada:** esquema estruturado em `items` e `auction_snapshots` com chaves estrangeiras  
- **Consultas Analíticas SQL:** agregações estatísticas (`AVG`, `MIN`, `ROUND`, `GROUP BY`, `JOIN`) para detecção de anomalias de preço  
- **Camada Cognitiva com LLM:** IA avalia risco de mercado, timing de liquidez e volume antes de recomendar o investimento  
- **Alertas Operacionais:** formatação assíncrona para consumo imediato mobile/desktop via Discord  

---

## Flow

Blizzard OAuth2 API → Python ETL Ingestion → PostgreSQL Storage → SQL Statistical Aggregations → Gemini LLM Market Analyst → Discord Trade Alert

---

## Business Logic

O algoritmo avalia oportunidades através de dois pilares:

- **Desvio Estatístico Quantitativo:** compara a menor oferta ativa com a média ponderada do banco de dados  
- **Avaliação Qualitativa por IA:** analisa liquidez de mercado, risco de patch/expansão e margem líquida pós-taxa da Auction House (corte de 5%)  

---

## Security

- credenciais sensíveis e chaves de API isoladas em `.env`  
- regras de segurança aplicadas via `.gitignore`  
- variáveis de ambiente documentadas através de `.env.example`  
- banco de dados containerizado com credenciais parametrizadas  

---

## Setup

1. Clonar repositório e acessar pasta:
   ```bash
   git clone [https://github.com/igorhsouza/wow-market-arbitrage-agent.git](https://github.com/igorhsouza/wow-market-arbitrage-agent.git)
   cd wow-market-arbitrage-agent

   Inicializar banco de dados:

Bash
docker compose up -d
Configurar variáveis de ambiente:

Bash
cp .env.example .env
(Preencher credenciais da Blizzard, Google Studio e Webhook do Discord no .env)

Instalar dependências:

Bash
pip install -r requirements.txt
Executar fluxo:

Bash
python fetch_market.py
python market_analyst.py
Notes
A tomada de decisão não é terceirizada cegamente para a IA.

A base do sistema apoia-se em dados matemáticos e consistência relacional em SQL.

O LLM atua estritamente como a camada de inteligência contextual e formulação de estratégia de saída.

Author
Igor Henrique

Automation • Data • Systems
