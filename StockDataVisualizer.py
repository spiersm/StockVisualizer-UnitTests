from SymbolInput import SymbolInput
from ChartTypeInput import ChartTypeInput
from Constants import Constants
from StockModel import StockModel
import requests as rq
import datetime
import pygal
import lxml

class StockDataVisualizer:
    """ Displays the graphs representing data from API call made using user inputs."""

    def __init__(self, inputData):
        """ Initalizes a stock data visualizer with the given dictionary where key is input constant and value is the user input. """
        self.inputData = inputData

    def queryStockData(self):
        """ Given a set of inputs performs a stock query """

        #API Query paramters
        series = "TIME_SERIES_" + Constants.TIMESERIES[self.inputData[Constants.SERIES]].upper()
        data = {
            "function": series,
            "symbol": self.inputData[Constants.SYMBOL],
            "outputsize":"full",
            "interval":"60min",
            "apikey":Constants.API_KEY
            }

        #Sending our request to the API using the information we put in the data collection.
        apiCall = rq.get(Constants.API_URL, params=data)

        #Stores the json-enconded content in the retrieved data.
        response = apiCall.json()
        
        # If statements to change key depending on the Time Serires selected. 
        if series == "TIME_SERIES_DAILY":
            timeSeries = "Time Series (Daily)"
        elif series == "TIME_SERIES_WEEKLY":
            timeSeries = "Weekly Time Series"
        elif series == "TIME_SERIES_MONTHLY":
            timeSeries = "Monthly Time Series"
        
        dates = []
        opens = []
        highs = []
        lows = []
        closes = []

        #Parsing the dates from the user input
        startDate = datetime.date.fromisoformat(self.inputData[Constants.STARTDATE])
        endDate = datetime.date.fromisoformat(self.inputData[Constants.ENDDATE])

        for date, stockData in reversed(response[timeSeries].items()):
            #Parsing the date from the api record.
            entryDate = datetime.date.fromisoformat(date)

            #Populating lists with data, within the given date range, from API 
            if (entryDate >= startDate and entryDate <= endDate):
                model = StockModel(stockData)
                opens.append(model.open)
                highs.append(model.high)
                lows.append(model.low)
                closes.append(model.close)
                dates.append(date)

        #If true, prints line chart. Else prints the bar chart.
        if self.inputData[Constants.CHARTTYPE] == "2":
            chart = pygal.Line(x_label_rotation=45)
            chart.x_labels = dates
            chart.title = "Stock Date for " + self.inputData[Constants.SYMBOL] + ": " + self.inputData[Constants.STARTDATE] + " to " + self.inputData[Constants.ENDDATE]
            chart.add("Open",opens)
            chart.add("High",highs)
            chart.add("Low", lows)
            chart.add("Close",closes)
            chart.render_in_browser()
            print("Success!")
        else:
            chart = pygal.Bar(x_label_rotation=45)
            chart.title = "Stock Date for " + self.inputData[Constants.SYMBOL] + ": " + self.inputData[Constants.STARTDATE] + " to " + self.inputData[Constants.ENDDATE]
            chart.x_labels = dates
            chart.add("Open",opens)
            chart.add("High",highs)
            chart.add("Low", lows)
            chart.add("Close",closes)
            chart.render_in_browser()
            print("Success!")




