import unittest
import main
from ChartTypeInput import ChartTypeInput
from Constants import Constants
from EndDateInput import EndDateInput
from StartDateInput import StartDateInput
import sys
import datetime
from StockDataVisualizer import StockDataVisualizer
from StockDataVisualizerInputs import StockDataVisualizerInputs
from StockModel import StockModel
from SymbolInput import SymbolInput
from TimeSeriesInput import TimeSeriesInput
from UserInput import UserInput
import requests as rq
import datetime
import pygal
import lxml
import requests

class TestStockData(unittest.TestCase):
    def setUp(self):
        print("set up")
        pass
    def tearDown(self):
        print("tear down")
        pass

    def test_stockSymbol(self):
        #Arrange StockSymbolInput "aaa"
        symbolInput_1 = SymbolInput("aaa")
        #Assert StockSymbolInput "aaa" works
        self.assertEqual(symbolInput_1.inputData[Constants.SYMBOL], "AAA")

        #Arrange StockSymbolInput "zzz"
        symbolInput_1 = SymbolInput("zzz")
        #Assert StockSymbolInput "zzz" won't work
        with self.assertRaises(ValueError):
            SymbolInput("zzz")

    def test_chartType(self):
        #Arrange ChartTypeInput "1" and "2"
        chartInput_1 = ChartTypeInput("1")
        chartInput_2 = ChartTypeInput("2")
        #Assert ChartTypeInput "1" and "2" work
        self.assertEqual(chartInput_1.inputData[Constants.CHARTTYPE], "1")
        self.assertEqual(chartInput_2.inputData[Constants.CHARTTYPE], "2")

        #Arrange ChartTypeInput "3"
        chartInput_3 = ChartTypeInput("3")
        #Assert ChartTypeInput "3" fails
        with self.assertRaises(ValueError):
            ChartTypeInput("3")


    def test_timeSeries(self):
        #Arrange TimeSeriesInput
        timeInput_1 = TimeSeriesInput("1")
        timeInput_2 = TimeSeriesInput("2")
        timeInput_3 = TimeSeriesInput("3")
        timeInput_4 = TimeSeriesInput("4")
        #Assert TimeSeriesInput 1-4 work
        self.assertEqual("TIME_SERIES_" + Constants.TIMESERIES[timeInput_1.inputData[Constants.SERIES]].upper(), "TIME_SERIES_INTRADAY")
        self.assertEqual("TIME_SERIES_" + Constants.TIMESERIES[timeInput_2.inputData[Constants.SERIES]].upper(), "TIME_SERIES_DAILY")
        self.assertEqual("TIME_SERIES_" + Constants.TIMESERIES[timeInput_3.inputData[Constants.SERIES]].upper(), "TIME_SERIES_MONTHLY")
        self.assertEqual("TIME_SERIES_" + Constants.TIMESERIES[timeInput_4.inputData[Constants.SERIES]].upper(), "TIME_SERIES_YEARLY")

        #Arrange ChartTypeInput "5"
        timeInput_5 = TimeSeriesInput("5")
        #Assert ChartTypeInput "5" fails
        with self.assertRaises(ValueError):
            TimeSeriesInput("5")

    def test_startDate(self):
        # Arrange StartDate "2020-01-01"
        startDate_1 = startDateInput("2020-01-01")
        # Act StartDate "2020-01-01" passes
        self.assertEqual(startDate_1.inputData[Constants.STARTDATE], "2020-01-01")

        # Arrange StartDate "2022-01-01"
        startDate_2 = startDateInput("2022-01-01")
        # Act StartDate "2022-01-01" fails
        with self.assertRaises(ValueError):
            startDateInput("2022-01-01")

        # Arrange StartDate "01-01-2020"
        startDate_3 = startDateInput("01-01-2020")
        # Act StartDate "01-01-2020" fails
        with self.assertRaises(ValueError):
            startDateInput("01-01-2020")

    def test_endDate(self):
        # Arrange StartDate "2020-01-01"
        endDate_1 = EndDateInput("2020-01-01")
        # Act StartDate "2020-01-01" passes
        self.assertEqual(endDate_1.inputData[Constants.ENDDATE], "2020-01-01")

        # Arrange StartDate "01-01-2020"
        endDate_2 = EndDateInput("01-01-2020")
        # Act StartDate "01-01-2020" fails
        with self.assertRaises(ValueError):
            endDateInput("01-01-2020")

    def test_again(self):
        # Arrange Again
        againInput_1 = "y"
        againInput_2 = "n"
        # Assert Again
        self.assertEqual(againInput_1.main.again, "y")
        self.assertEqual(againInput_2.main.again, "n")

        #Arrange AgainInput "a"
        againInput_3 = "n"
        #Assert AgainInput "a" fails
        with self.assertRaises(ValueError):
            againInput_3.main.again == "a"

if __name__ == "__main__":
    unittest.main()



