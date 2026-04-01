import requests

url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"

def cotacao_dolar():
    """🔥 Busca cotação do dólar em tempo real"""
    try:
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            dolar = float(data["USDBRL"]["bid"])
            return dolar
        else:
            print("❌ Erro na API (Status:", response.status_code, ")")
            return 5.50  # Valor padrão
    except Exception as e:
        print("❌ Erro ao buscar cotação:", e)
        return 5.50  # Valor padrão