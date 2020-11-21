from SymbolInput import SymbolInput
from ChartTypeInput import ChartTypeInput
from TimeSeriesInput import TimeSeriesInput
from StartDateInput import StartDateInput
from EndDateInput import EndDateInput
from Constants import Constants


class StockDataVisualizerInputs:
    """ Object for registering user input objects which will be iterated over and collected."""
    def __init__(self):

        startDateInput = StartDateInput()
        
        self.userInputs = {
            Constants.SYMBOL: SymbolInput(),
            Constants.CHARTTYPE: ChartTypeInput(),
            Constants.SERIES: TimeSeriesInput(),
            Constants.STARTDATE: startDateInput,
            Constants.ENDDATE: EndDateInput(startDateInput)
        }

    def gatherUserInput(self):
        """ 
        Using the required self.userInputs, prompts user for required inputs and validates provided values. 
        Valid inputs are returned in a dictionary {key: constant, value: validated user input} 
        """
        kvp = {}
        # For each user input object 
        for key, ui in self.userInputs.items():
            while True:
                #display the optional options txt to display valid options to the user
                print("\r\n" + ui.optionsTxt)
                
                # Prompt the user for valid input
                userInput = input(ui.promptMsg + ":")
                
                # try to set the value which will validate the input
                if(ui.trySetValue(userInput)):
                    # if input is valid move on
                    break
                else:
                    # If input is invalid notify user and continue looping asking for valid input.
                    print("Value '" + userInput + "' is not valid.")
            
            # add validated value to return value
            kvp.update({key: ui.value})
        
        return kvp