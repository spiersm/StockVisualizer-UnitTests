from UserInput import UserInput
from Constants import Constants

class ChartTypeInput(UserInput):
    
    def __init__(self):
        """Chart Type input constructor"""
            
        # The example txt displayed to the user on input request
        exampletxt = ("Chart Types\r\n" +
                     "=============\r\n")
        for key, value in Constants.CHARTTYPES.items():
            exampletxt += key + ". " + value + "\r\n"
            
        # Call base constructor initalizing prompt message and example txt
        UserInput.__init__(
            self, 
            "Enter the chart type you want (1, 2)",
            exampletxt)

    def isInputValid(self, input):
        if (input == "1"):
            return True
        elif (input == "2"):
            return True
        else:
            print("Please enter 1 or 2")
            return False

