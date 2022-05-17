# Error called specifically when input is incorrect (General Case)
class IncorrectInput(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message