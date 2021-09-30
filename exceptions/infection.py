class InfectionException(Exception):
    message = "Cannot infect this agent"

    def __init__(self):
        print(self.message)
