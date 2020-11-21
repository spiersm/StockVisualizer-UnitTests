from UserInput import UserInput
import requests 
from Constants import Constants
class SymbolInput(UserInput):
    
    def __init__(self):
        """Symbol input constructor"""
        UserInput.__init__(
            self, 
            "Enter the stock symbol you are looking for")

    def isInputValid(self, symbol):
        """The shared validate input function."""
        # Query paramaters
        data = {
            "function":Constants.SYMBOL_SEARCH,
            "keywords":symbol,
            "apikey":Constants.API_KEY
        }

        # Query symbol search API
        apiCall = requests.get(Constants.API_URL, params=data)
        response = apiCall.json()

        # for each returned match 
        matches = []
        for match in response["bestMatches"]:
            # if an exact match symbol is valid; return true
            if(match["1. symbol"].upper() == symbol.upper()):
                return True
            else:
                matches.append(match["1. symbol"])
            
        # if not an exact match, display best matches from the api
        print(f'{symbol} was not found. Did you mean {", ".join(matches)}?')
        return False



