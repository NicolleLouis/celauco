from mesa import Model
from mesa.time import RandomActivation

from model.agent import CelaucoAgent


class CelaucoModel(Model):
    """A model with some number of agents."""
    def __init__(self, agents_number):
        self.num_agents = agents_number
        self.schedule = RandomActivation(self)
        # Create agents
        for i in range(self.num_agents):
            agent = CelaucoAgent(i, self)
            self.schedule.add(agent)

    def step(self):
        """Advance the model by one step."""
        self.schedule.step()
