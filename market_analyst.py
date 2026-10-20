import os
import requests
import psycopg2
from dotenv import load_dotenv
from google import genai

load_dotenv()

DB_HOST = "localhost"
DB_PORT = 5432
DB_NAME = "wow_market"
DB_USER = "admin"
DB_PASS = "supersecretpassword"

DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

def send_to_discord(report_text):
    """Envia o relatório gerado pela IA direto para o canal do Discord"""
    if not DISCORD_WEBHOOK_URL:
        print("⚠️ DISCORD_WEBHOOK_URL não configurada no .env")
        return
    
    # O Discord aceita mensagens de até 2000 caracteres por envio
    payload = {
        "username": "Goblin Market Analyst",
        "avatar_url": "https://render.worldofwarcraft.com/us/icons/56/inv_misc_coin_01.jpg",
        "content": f"🔔 **NOVA ANÁLISE DE MERCADO DA AUCTION HOUSE** 🔔\n\n{report_text}"
    }
    
    response = requests.post(DISCORD_WEBHOOK_URL, json=payload)
    if response.status_code in [200, 204]:
        print("✅ Relatório enviado com sucesso para o Discord!")
    else:
        print(f"❌ Erro ao enviar para o Discord: {response.status_code} - {response.text}")

def analyze_market_with_ai():
    conn = psycopg2.connect(
        host=DB_HOST, port=DB_PORT, dbname=DB_NAME, user=DB_USER, password=DB_PASS
    )
    cursor = conn.cursor()
    
    query = """
        SELECT 
            i.name,
            ROUND(AVG(a.unit_price) / 10000.0, 2) AS preco_medio,
            ROUND(MIN(a.unit_price) / 10000.0, 2) AS menor_preco,
            SUM(a.quantity) AS volume_disponivel
        FROM auction_snapshots AS a
        JOIN items AS i ON a.item_id = i.item_id
        WHERE a.item_id = 191471
        GROUP BY i.name;
    """
    
    cursor.execute(query)
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    
    if not result:
        print("Nenhum dado encontrado no banco.")
        return

    item_name, avg_price, min_price, total_qty = result
    desconto_percentual = round(((avg_price - min_price) / avg_price) * 100, 1)
    
    print("🤖 Consultando o Agente de Inteligência Artificial...")
    
    client = genai.Client()
    prompt = f"""
    Aja como um especialista em arbitragem e economia do World of Warcraft. Seja divertido e pé no chão, pode fazer piadas.
    
    Analise os seguintes dados coletados da Auction House:
    - Item: {item_name}
    - Preço Médio no Banco: {avg_price}g
    - Menor Oferta Agora: {min_price}g
    - Volume em Estoque: {total_qty} unidades
    - Desconto em relação à média: {desconto_percentual}%
    
    Formate para leitura rápida no Discord (use negrito e emojis):
    1. **Veredito**: [COMPRAR / AGUARDAR / VENDER]
    2. **Risco & Margem**: Resumo curto
    3. **Ação Recomendada**: O que o jogador deve fazer agora
    """
    
    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt
    )
    
    ai_report = response.text
    print("\n" + ai_report)
    
    # Dispara o webhook
    send_to_discord(ai_report)

if __name__ == "__main__":
    analyze_market_with_ai()