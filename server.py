import sys
import json

from flask import Flask, Response, render_template, request, jsonify
from flask_cors import CORS
from api.stocks import Stocks

app = Flask(__name__, template_folder = 'html/static')

CORS(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/_search', methods=['POST'])
def search():
    stocksResult = stocks.get_avaiable_stocks(request.form.get('stock_filter'))
    return Response(json.dumps(stocksResult), mimetype='application/json')

if len(sys.argv) > 1:
    apikey = sys.argv[1]
    stocks = Stocks(apikey)
    PORT = 5000
    app.run(port = PORT)
else:
    # API key can be found at https://www.alphavantage.co/support/#api-key
    print('Api key not found.')
