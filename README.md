#  WoW Auction House Market Arbitrage Agent

An automated market intelligence and arbitrage detection pipeline that extracts real-time World of Warcraft commodity auction data, persists time-series snapshots into PostgreSQL, and leverages Google Gemini (LLM) to perform quantitative financial analysis and deliver actionable trade alerts via Discord.

##  Architecture Overview

```text
[Blizzard OAuth2 API] 
       ↓ (Ingests ~300k live commodity auctions)
[Python ETL Worker] 
       ↓ (Filters items, normalizes copper-to-gold pricing)
[PostgreSQL (Docker)] 
       ↓ (Stores relational snapshots, runs statistical aggregations)
[Gemini LLM Agent] 
       ↓ (Analyzes risk/reward, patch cycle dynamics & market margins)
[Discord Webhook] (Delivers executive buy/sell reports)

### Tech Stack
Language & Runtimes: Python 3.10+, Docker, PostgreSQL 15

APIs & Protocols: Blizzard Battle.net OAuth2 REST API, Google GenAI SDK, Discord Webhooks

Libraries: psycopg2-binary, requests, python-dotenv, google-genai

Database Tooling: DBeaver, Docker Compose

#### Setup & Installation
Clone the repository: git clone [https://github.com/SEU_USUARIO/wow-market-arbitrage-agent.git](https://github.com/SEU_USUARIO/wow-market-arbitrage-agent.git)
cd wow-market-arbitrage-agent

Spin up the database:

Bash
docker compose up -d
Configure Environment Variables:
Copy .env.example to .env and fill in your API credentials:

Bash
cp .env.example .env
Install Dependencies:

Bash
pip install -r requirements.txt
Run Data Ingestion & AI Analysis:

Bash
python fetch_market.py
python market_analyst.py