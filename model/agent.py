from mesa import Agent

from constants.player_state import InfectionState, InfectionKnowledgeState
from service.grid import GridService
from service.movement import MovementService
from service.probability import ProbabilityService


class CelaucoAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.infection_state = InfectionState.HEALTHY
        self.infection_knowledge_state = InfectionKnowledgeState.UNAWARE
        self.infection_duration = 0

    def step(self):
        self.move()
        if self.is_infected():
            self.infect_neighbours()
            self.infection_evolution()

    def move(self):
        if self.infection_knowledge_state == InfectionKnowledgeState.AWARE:
            new_position = MovementService.avoid_agents(agent=self)
        else:
            new_position = MovementService.random_move(agent=self)
        self.model.grid.move_agent(self, new_position)

    def infection_evolution(self):
        self.infection_duration += 1
        if self.infection_duration >= self.model.infection_duration:
            self.set_immune()
        else:
            if ProbabilityService.random_probability(self.model.death_probability):
                self.set_dead()

    def infect_neighbours(self):
        neighbours = GridService.get_grid_content(
            grid=self.model.grid,
            positions=self.get_neighbour_positions()
        )
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
        return GridService.get_neighbour_position(
            grid=self.model.grid,
            position=self.pos
        )

    def set_infected(self):
        if self.infection_state != InfectionState.HEALTHY:
            raise SystemError("Cannot infect this agent")
        self.infection_state = InfectionState.INFECTED
        self.infection_knowledge_state = InfectionKnowledgeState.AWARE

    def is_infected(self):
        return self.infection_state == InfectionState.INFECTED

    def is_healthy(self):
        return self.infection_state == InfectionState.HEALTHY

    def is_immune(self):
        return self.infection_state == InfectionState.IMMUNE

    def set_immune(self):
        if self.infection_state != InfectionState.INFECTED:
            raise SystemError("A non infected agent cannot become immune")
        self.infection_state = InfectionState.IMMUNE
        self.infection_knowledge_state = InfectionKnowledgeState.UNAWARE

    def set_dead(self):
        if self.infection_state != InfectionState.INFECTED:
            raise SystemError("A non infected agent cannot die")
        self.infection_state = InfectionState.DEAD
        self.model.kill_agent(agent=self)

    def display(self):
        """
        Documentation is in the class: CanvasGrid(VisualizationElement)
        file: CanvasGridVisualization from mesa.visualization.modules
        """
        data = {
            "Shape": "circle",
            "Color": "green",
            "Filled": "false",
            "Layer": 0,
            "r": 0.5,
            "w": 0.5,
            "h": 0.5,
            "text_color": "white"
        }
        if self.infection_state == InfectionState.INFECTED:
            data["Color"] = "red"
        if self.infection_state == InfectionState.IMMUNE:
            data["Color"] = "blue"

        if self.infection_knowledge_state == InfectionKnowledgeState.AWARE:
            data["Shape"] = "rect"
        return data
