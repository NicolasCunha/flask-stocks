import requests
import json

class Stocks:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_avaiable_stocks(self, term):
        # The following is the URL for a symbol search (stock "code")
        url = "https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={}&apikey={}"
        # Format the URL to contain the term to be searched, as well as the API key that was
        # defined when starting the server.
        url = url.format(term, self.api_key)
        # Execute a GET request
        result = requests.get(url)
        if(result != None):
            # Trasnform the JSON to a Python dictionary
            resultDict = json.loads(result.text)
            responseDict = {}
            i = 0
            try:
                # Each entry in "bestMatches" is a stock
                for match in resultDict["bestMatches"]:
                    dictEntry = {"code": match["1. symbol"], "name" : match["2. name"], "region": match["4. region"]}
                    responseDict.update({i : dictEntry})
                    i = i + 1
            except:
                # Alpha Vantage Free API has a limit of 5 request per minute, 500 per day.
                responseDict.update({0 : {"code": 404, "name": "API NOT AVAIABLE", "region" : "N/A"}})
            return responseDict
        # If no result was found, return a empty array
        return ['']


