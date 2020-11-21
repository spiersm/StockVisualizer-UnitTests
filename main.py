import sys
from StockDataVisualizer import StockDataVisualizer
from StockDataVisualizerInputs import StockDataVisualizerInputs
from Constants import Constants

# Main program loop 
# Intializes and executes a stock query then prompts user
# if they want a redo.
while True:
    print("Stock Data Visualizer\r\n" +
    "===============================")

    # Gathering user inputs
    inputs = StockDataVisualizerInputs()
    values = inputs.gatherUserInput()

    # Using the gathered inputs to query stock data from the api
    s = StockDataVisualizer(values)
    s.queryStockData()
    
    
    while True:
        again = input("Would you like to view more stock data? ('Y' or 'N'):").lower()
        if(again == 'y'):
            break
        elif(again != 'n'):
            print("'" + again + "' is not a valid value.")
        else:
            sys.exit(0)