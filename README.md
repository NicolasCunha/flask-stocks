# Stocks search and daily/weekly/monthly quotation/values
This is a sample project to put in practice Python and Flask knowledge.

# How to execute?

To execute this project, you need an API key from Alpha Vantage. You can get one for free (with the limit of 5 requests per minute, 500 per day) [here](https://www.alphavantage.co/support/#api-key).

```python
python server.py <API_KEY>
```

# Avaiable endpoints

/_search:
    Receives a request value "stock_filter" with the stock symbol to be searched.
    It will return a list of the stocks that includes that symbol.

/_get_prices:
    Receives a request value "stock_filter" with the stock symbol from which values will be searched from.
    It will return a list of the past seven days highs and lows, past seven weeks highs and lows and past six months highs and lows.