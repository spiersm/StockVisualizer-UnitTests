from UserInput import UserInput
from Constants import Constants
#Time Series Function Input
class TimeSeriesInput(UserInput):
    def __init__(self):
        """Chart Type input constructor"""
            
        # The example txt displayed to the user on input request
        exampletxt = ("Select the Time Series of the chart you want to Generate\r\n" +
                     "--------------------------------------------------------\r\n")
        for key, value in Constants.TIMESERIES.items():
            exampletxt += key + ". " + value + "\r\n"
            
        # Call base constructor initalizing prompt message and example txt
        UserInput.__init__(
            self, 
            "Enter time series option (1, 2, 3, 4)",
            exampletxt)

    def isInputValid(self, timeSeries):
        try:
            selection = int(timeSeries)
            if(selection < 1 or selection > 4):
                print("\nThe input you entered is invalid. Please enter one of the four options.\n")
                return False
        except ValueError:
            print("\nThe value you entered is not an integer. Please enter one of the four options.\n")
            return False

        return True

    
