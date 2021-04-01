import requests
import json
import logging

# The following URL's are the default for a get requests
# They can be found in Alpha Vantage's documentation https://www.alphavantage.co/documentation/
SEARCH_DEFAULT_URL = "https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={}&apikey={}"
DAILY_VALUE_DEFAULT_URL = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={}&outputsize=compact&apikey={}"
WEEKLY_VALUE_DEFAULT_URL = "https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol={}&outputsize=compact&apikey={}"
MONTHLY_VALUE_DEFAULT_URL = "https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol={}&outputsize=compact&apikey={}"

class Stocks:

    def __init__(self, api_key):
        self.api_key = api_key

    def get_avaiable_stocks(self, term):
        # Format the URL to contain the term to be searched, as well as the API key that was
        # defined when starting the server.
        url = SEARCH_DEFAULT_URL.format(term, self.api_key)
        # Execute a GET request
        result = requests.get(url)
        if(result != None):
            # Transform the JSON to a Python dictionary
            resultDict = json.loads(result.text)
            responseDict = {}
            i = 0
            try:
                # Each entry in "bestMatches" is a stock
                for match in resultDict["bestMatches"]:
                    dictEntry = {
                        "code": match["1. symbol"], 
                        "name" : match["2. name"], 
                        "region": match["4. region"]
                    }
                    responseDict.update({i : dictEntry})
                    i = i + 1
            except Exception:
                # Alpha Vantage Free API has a limit of 5 request per minute, 500 per day.
                responseDict.update({"error": True, "desc": "Api is not avaiable. Alpha Vantage Free API has a limit of 5 request per minute, 500 per day."})
                logging.exception("Exception")
            return responseDict
        # If no result was found, return a empty array
        return ['']

    def copy_dict_to_self(self, tag, dict):
        newDict = {tag : dict}
        return newDict

    def get_value_url(self, extUrl, term, tag, responseTag):
        # Format the URL to contain the term to be searched, as well as the API key that was
        # defined when starting the server.
        url = extUrl.format(term, self.api_key)
        # Execute a GET request
        result = requests.get(url)
        if (result != None):
            # Transform the JSON to a Python dictionary
            resultDict = json.loads(result.text)
            responseDict = {}        
            i = 0
            try:
                # Each entry in "tag" is a result
                # "[:7]" retrives the first 7 seven values in the list
                for match in list(resultDict[tag].items())[:7]:
                    values = match[1]
                    dictEntry = {
                        "date" : match[0],
                        "open" : values["1. open"], 
                        "high" : values["2. high"], 
                        "low" : values["3. low"], 
                        "close": values["4. close"], 
                        "volume": values["5. volume"]
                    }
                    responseDict.update({i : dictEntry})
                    i = i + 1
                responseDict = self.copy_dict_to_self(responseTag, responseDict)
            except Exception:
                # Alpha Vantage Free API has a limit of 5 request per minute, 500 per day.
                responseDict.update({"error": True, "desc": "Api is not avaiable. Alpha Vantage Free API has a limit of 5 request per minute, 500 per day."})
                logging.exception("Exception")
            return responseDict
        # If no result was found, return a empty array
        return ['']

    def get_values(self, term):
        result = {}
        daily = self.get_value_url(DAILY_VALUE_DEFAULT_URL, term, "Time Series (Daily)", "daily")
        weekly = self.get_value_url(WEEKLY_VALUE_DEFAULT_URL, term, "Weekly Time Series", "weekly")
        monthly = self.get_value_url(MONTHLY_VALUE_DEFAULT_URL, term, "Monthly Time Series", "monthly")
        result.update(daily)
        result.update(weekly)
        result.update(monthly)
        return result



