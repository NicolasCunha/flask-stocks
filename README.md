# Stocks
This is a simple project to put in practice Python and Flask knowledge, consuming a stocks API to search, retrieve and display it's values.

# How to execute?

Install the dependencies.

```python
pip install -r requirements.txt
```

To execute this project, you need an API key from Alpha Vantage. You can get one for free (with the limit of 5 requests per minute, 500 per day) [here](https://www.alphavantage.co/support/#api-key).

```python
python server.py <API_KEY>
```

# Avaiable endpoints

## /_search

Receives a request value "stock_filter" with the stock symbol to be searched.
It will return a list of the stocks that includes that symbol.

## /_get_values

Receives a request value "stock_filter" with the stock symbol from which values will be searched from.
It will return a list of the past seven days values, past seven weeks values and past seven months values.
