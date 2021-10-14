from model.human_agents.base_human import BaseHuman
from service.movement import MovementService


class GiletJosne(BaseHuman):
    def next_position(self):
        new_position = MovementService.search_agents(agent=self)
        return new_position

    def display(self):
        data = super().display()
        data["scale"] = 0.9
        data["Layer"] = 0.5
        # data["Shape"] = "images/beer"
        if self.is_healthy():
            data["Shape"] = "images/gilet_josne"
        if self.is_infected():
            data["Shape"] = "images/gilet_josne_infected"
        return data
