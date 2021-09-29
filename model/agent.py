from mesa import Agent


class CelaucoAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

    def step(self):
        print("Hi, I am agent " + str(self.unique_id) + ".")
