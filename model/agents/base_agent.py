from mesa import Agent

from constants.player_state import InfectionState, InfectionKnowledgeState
from exceptions.infection import InfectionException
from service.grid import GridService
from service.movement import MovementService
from service.probability import ProbabilityService


class CelaucoAgent(Agent):
    """
    Base Agent class, function to override:
    - move()
    - additional_step()
    - display()
    """

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.infection_state = InfectionState.HEALTHY
        self.infection_knowledge_state = InfectionKnowledgeState.UNAWARE
        self.infection_duration = 0

    def step(self):
        self.move()
        self.additional_step()
        if self.is_infected():
            self.infect_neighbours()
            self.infection_evolution()

    def move(self):
        new_position = self.next_position()
        self.model.grid.move_agent(self, new_position)

    def next_position(self):
        if self.is_infected() and self.is_aware():
            new_position = MovementService.avoid_agents(agent=self)
        else:
            new_position = MovementService.random_move(agent=self)
        return new_position

    def infection_evolution(self):
        self.infection_duration += 1
        if self.infection_duration >= self.model.infection_duration:
            self.set_immune()
        else:
            if ProbabilityService.random_probability(self.model.death_probability):
                self.set_dead()

    def infect_neighbours(self):
        neighbours = self.get_neighbors()
        can_be_infected_neighbours = list(
            filter(
                lambda neighbour: neighbour.can_be_infected(),
                neighbours
            )
        )
        for neighbour in can_be_infected_neighbours:
            if ProbabilityService.random_probability(self.model.infection_probability):
                neighbour.set_infected()

    def get_neighbors(self):
        neighbours = GridService.get_grid_content(
            grid=self.model.grid,
            positions=GridService.get_agent_neighbour_position(
                agent=self
            )
        )
        return neighbours

    def can_be_infected(self):
        return self.infection_state == InfectionState.HEALTHY

    def set_infected(self):
        if not self.can_be_infected():
            raise InfectionException()
        self.infection_state = InfectionState.INFECTED

    def is_infected(self):
        return self.infection_state == InfectionState.INFECTED

    def is_healthy(self):
        return self.infection_state == InfectionState.HEALTHY or self.infection_state == InfectionState.IMMUNE

    def is_immune(self):
        return self.infection_state == InfectionState.IMMUNE

    def is_unaware(self):
        return self.infection_knowledge_state == InfectionKnowledgeState.UNAWARE

    def is_aware(self):
        return self.infection_knowledge_state == InfectionKnowledgeState.AWARE

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

    def set_aware(self):
        self.infection_knowledge_state = InfectionKnowledgeState.AWARE

    def additional_step(self):
        """
        function used to add additional step executed by agent
        :return:
        """
        pass

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
            data["Color"] = "yellow"

        return data
