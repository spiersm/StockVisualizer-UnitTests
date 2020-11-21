import datetime
from UserInput import UserInput
from Constants import Constants

class StartDateInput(UserInput):

    def __init__(self):

        UserInput.__init__(self,"Enter the start date (YYYY-MM-DD)")

    def isInputValid(self, input):
        try:
            datetime.date.fromisoformat(input)
            return True

        except ValueError:
            return False