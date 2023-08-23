import requests
from datetime import datetime, timedelta

def get_historical_prices():
    end_date = datetime.now()
    start_date = end_date - timedelta(days=30)

    url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart/range"
    params = {
        "vs_currency": "usd",
        "from": int(start_date.timestamp()),
        "to": int(end_date.timestamp())
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        prices = data["prices"]
        return prices
    else:
        print("Failed to retrieve historical prices.")
        return None

def calculate_average_price(prices):
    total_price = sum(price for timestamp, price in prices)
    average_price = total_price / len(prices)
    return average_price

if __name__ == "__main__":
    historical_prices = get_historical_prices()

    if historical_prices is not None:
        average_price = calculate_average_price(historical_prices)
        print(f"Average Bitcoin Price (last 30 days): ${average_price:.2f}")

