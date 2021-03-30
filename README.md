# Stocks search and daily/weekly/monthly quotation/values
This is a sample project to put in practice Python and Flask knowledge.

# How to execute?

To execute this project, you need an API key from Alpha Vantage. You can get one for free (with the limit of 5 requests per minute, 500 per day) [here](https://www.alphavantage.co/support/#api-key).

# Avaiable endpoints

/_search:
    Receives a form "stock_filter" with the stock symbol to be searched.
    It will return a list of the stocks that includes that symbol.    

```python
python server.py <API_KEY>
```