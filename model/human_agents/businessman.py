from model.human_agents.base_human import BaseHuman
from service.movement import MovementService
from service.probability import ProbabilityService


class BusinessMan(BaseHuman):
    flight_probability = 5

    def __init__(self, *args):
        super().__init__(*args)
        self.is_flying = False

    def next_position(self):
        if ProbabilityService.random_percentage(self.flight_probability):
            self.set_flying()
            return MovementService.random_position(agent=self)
        self.set_walking()
        return super().next_position()

    def set_flying(self):
        self.is_flying = True

    def set_walking(self):
        self.is_flying = False

    def display(self):
        data = super().display()
        if self.is_flying:
            data["scale"] = 1
            data["Layer"] = 1
            if self.is_healthy():
                data["Shape"] = "images/plane"
            if self.is_infected():
                data["Shape"] = "images/plane_infected"
        return data
