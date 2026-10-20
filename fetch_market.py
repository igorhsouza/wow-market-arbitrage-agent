import os
import requests
import psycopg2
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = "54abe57134c84634ba8686f7407c795c"
CLIENT_SECRET = "CeRinncXFUPk5FKKei1rD1eHj45qXKQe"

# Dados de conexão com o PostgreSQL do Docker
DB_HOST = "localhost"
DB_PORT = 5432
DB_NAME = "wow_market"
DB_USER = "admin"
DB_PASS = "supersecretpassword"

def get_access_token():
    url = "https://oauth.battle.net/token"
    data = {"grant_type": "client_credentials"}
    response = requests.post(url, data=data, auth=(CLIENT_ID, CLIENT_SECRET))
    if response.status_code == 200:
        return response.json().get("access_token")
    return None

def fetch_and_save_deals(token, target_item_id=191471):
    url = "https://us.api.blizzard.com/data/wow/auctions/commodities"
    params = {"namespace": "dynamic-us", "locale": "en_US"}
    headers = {"Authorization": f"Bearer {token}"}
    
    print("Baixando leilões ativos da Blizzard...")
    response = requests.get(url, params=params, headers=headers)
    if response.status_code != 200:
        print("Erro na requisição da Blizzard.")
        return
    
    auctions = response.json().get("auctions", [])
    
    # Filtra os leilões do item escolhido
    deals = [auc for auc in auctions if auc.get("item", {}).get("id") == target_item_id]
    deals.sort(key=lambda x: x.get("unit_price", float("inf")))
    
    # Pega apenas os 10 melhores preços para salvar no snapshot
    top_deals = deals[:10]
    
    print(f"Encontrados {len(deals)} lotes. Gravando os top 10 no banco de dados...")
    
    # Conecta no PostgreSQL
    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )
    cursor = conn.cursor()
    
    # Insere cada leilão na tabela auction_snapshots
    insert_query = """
        INSERT INTO auction_snapshots (item_id, unit_price, quantity)
        VALUES (%s, %s, %s);
    """
    
    for deal in top_deals:
        unit_price = deal.get("unit_price")
        quantity = deal.get("quantity")
        cursor.execute(insert_query, (target_item_id, unit_price, quantity))
        
    conn.commit()
    cursor.close()
    conn.close()
    
    print("✅ Dados gravados com sucesso no PostgreSQL!")

if __name__ == "__main__":
    token = get_access_token()
    if token:
        fetch_and_save_deals(token, target_item_id=191471)