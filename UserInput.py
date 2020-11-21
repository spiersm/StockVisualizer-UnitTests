class UserInput:
    def __init__(self, promptMsg, optionsTxt=""):
        # The message displayed to the user specifying the value being requested.
        self.promptMsg = promptMsg

        # (Optional) A formatted string optionally providing the valid options to the user.
        self.optionsTxt = optionsTxt

        # Intilize the value property which will contain the validated user input.
        self.value = None

    def trySetValue(self, input):
        """ The method called when user input is received that calls the validate input function
        and returns whether the input is valid or not. If input is valid, it sets self.value equal to input. """
        if (self.isInputValid(input)):
            self.value = input
            return True
        else:
            return False

    def isInputValid(self, input):
        """
        Abstract method that MUST be implemented on inheriting user input types.
        Given the input invokes the specified validate function returning true if input is valid.
        """
        pass
    
