import requests

# Fetch conversion rates from CoinMarketCap API
def convert_crypto(amount, from_currency, to_currency, api_key):
    url = "https://pro-api.coinmarketcap.com/v1/tools/price-conversion"
    headers = {"X-CMC_PRO_API_KEY": api_key}
    params = {
        "amount": amount,
        "symbol": from_currency,
        "convert": to_currency
    }
    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    if response.status_code == 200 and "data" in data:
        return data["data"]["quote"][to_currency]["price"]
    else:
        return None, data.get("status", {}).get("error_message", "Error occurred")
