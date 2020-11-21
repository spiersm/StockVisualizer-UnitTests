import datetime
from UserInput import UserInput

class EndDateInput(UserInput):
    #passing in the start date provided by user
    def __init__(self, startDateInput):
        self.startDateInput = startDateInput
        UserInput.__init__(self, "Enter the end Date (YYYY-MM-DD)")

    def isInputValid(self, endDate):
        #try block to catch value errors
        try:
            #splitting input to use with datetime module
            d1 = self.startDateInput.value.split(('-'))
            d2 = endDate.split('-')
            #creating datetime objects
            start = datetime.datetime(int(d1[0]),int(d1[1]),int(d1[2]))
            end = datetime.datetime(int(d2[0]),int(d2[1]),int(d2[2]))
            #error handling for end date before start date
            if start == end:
                print("[ERROR] Start date cannot be the same as end date\n")
            elif start > end:
                print("[ERROR] Start date cannot be after end date\n")
            else:
                return True
        except ValueError:
            print("[ERROR] Invalid date provided.\n")
        
        # Date is invalid
        return False

#Error checking and example use
#date = dateValidator("1999-06-29")
#endDate = date.endDate()