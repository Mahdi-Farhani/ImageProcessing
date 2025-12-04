class GeneralUtility:
    @staticmethod
    def UserInput(prompt: str,default:"str") -> str:
        """Get user input from the console."""
        user_input= input(prompt)
        value = user_input if user_input.strip() !="" else default
        return value