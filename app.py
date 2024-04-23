from flask import Flask, render_template
import requests

app = Flask(__name__)

# Alpha Vantage API URL and API key
API_KEY = 'YOUR_API_KEY'
API_URL = 'https://www.alphavantage.co/query'

@app.route('/')
def homepage():
    symbol = 'AAPL'  # Example stock symbol
    price = fetch_stock_price(symbol)
    if price is not None:
        return render_template('homepage.html', symbol=symbol, price=price)
    else:
        return "Failed to fetch stock price data."

def fetch_stock_price(symbol):
    params = {
        'function': 'GLOBAL_QUOTE',
        'symbol': symbol,
        'apikey': API_KEY
    }
    response = requests.get(API_URL, params=params)
    data = response.json()
    if 'Global Quote' in data:
        return data['Global Quote']['05. price']
    else:
        return None

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
