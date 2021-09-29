from mesa import Agent

from constants.player_state import AgentState
from service.probability import ProbabilityService


class CelaucoAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.state = AgentState.HEALTHY
        self.infection_duration = 0

    def step(self):
        self.move()
        if self.is_infected():
            self.infect_neighbours()
            self.infection_evolution()

    def move(self):
        new_position = self.random.choice(self.get_neighbour_positions())
        self.model.grid.move_agent(self, new_position)

    def infection_evolution(self):
        self.infection_duration += 1
        if self.infection_duration >= self.model.infection_duration:
            self.set_immune()

    def infect_neighbours(self):
        neighbours = self.model.grid.get_cell_list_contents(self.get_neighbour_positions())
        healthy_neighbours = list(
            filter(
                lambda neighbour: neighbour.is_healthy(),
                neighbours
            )
        )
        for neighbour in healthy_neighbours:
            if ProbabilityService.random_probability(self.model.infection_probability):
                neighbour.set_infected()

    def get_neighbour_positions(self):
        neighbor_positions = self.model.grid.get_neighborhood(
            self.pos,
            moore=True,
            include_center=True,
        )
        return neighbor_positions

    def set_infected(self):
        if self.state != AgentState.HEALTHY:
            raise SystemError("Cannot infect this agent")
        self.state = AgentState.INFECTED

    def is_infected(self):
        return self.state == AgentState.INFECTED

    def is_healthy(self):
        return self.state == AgentState.HEALTHY

    def is_immune(self):
        return self.state == AgentState.IMMUNE

    def set_immune(self):
        if self.state != AgentState.INFECTED:
            raise SystemError("A non infected agent cannot become immune")
        self.state = AgentState.IMMUNE

    def display(self):
        data = {
            "Shape": "circle",
            "Color": "green",
            "Filled": "true",
            "Layer": 0,
            "r": 0.5,
        }
        if self.state == AgentState.INFECTED:
            data["Color"] = "red"
        if self.state == AgentState.IMMUNE:
            data["Color"] = "blue"
        return data
