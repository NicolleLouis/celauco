from model.agents.base_agent import CelaucoAgent
from service.movement import MovementService


class GiletJosne(CelaucoAgent):
    def next_position(self):
        new_position = MovementService.search_agents(agent=self)
        return new_position

    def display(self):
        data = super().display()
        data["scale"] = 0.9
        data["Layer"] = 0.5
        if self.is_healthy():
            data["Shape"] = "images/gilet_josne"
        if self.is_infected():
            data["Shape"] = "images/gilet_josne_infected"
        return data
