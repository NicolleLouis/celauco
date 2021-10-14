from mesa import Agent

from constants.player_state import InfectionState, InfectionKnowledgeState
from exceptions.infection import InfectionException
from service.grid import GridService
from service.infection_service import InfectionService
from service.movement import MovementService
from service.probability import ProbabilityService


class BaseHuman(Agent):
    """
    Base Human class, function to override:
    - move()
    - additional_step()
    - display()
    """

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.infection = None
        self.infection_state = InfectionState.HEALTHY
        self.infection_knowledge_state = InfectionKnowledgeState.UNAWARE
        self.lockdown = False
        self.infection_duration = 0
        self.immunity = []

    def step(self):
        self.move()
        self.additional_step()
        if self.is_infected():
            self.infect_neighbours()
            self.infection_mutation()
            self.infection_evolution()

    def move(self):
        new_position = self.next_position()
        self.model.grid.move_agent(self, new_position)

    def next_position(self):
        if self.lockdown:
            new_position = MovementService.avoid_agents(agent=self)
        else:
            new_position = MovementService.random_neighbours(agent=self)
        return new_position

    def infection_mutation(self):
        if ProbabilityService.random_probability_1000(self.infection.mutation_probability):
            new_infection = InfectionService.generate_infection(self.infection)
            self.infection = new_infection
            self.model.add_known_infection(new_infection)

    def infection_evolution(self):
        self.infection_duration += 1
        self.infection.infection_score += 1
        # Immunity
        if self.infection_duration >= self.infection.infection_duration:
            self.set_immune(self.infection)
        # Death
        else:
            if ProbabilityService.random_probability_1000(self.infection.death_probability):
                self.set_dead()

    def infect_neighbours(self):
        neighbours = self.get_neighbors()
        can_be_infected_neighbours = list(
            filter(
                lambda neighbour: neighbour.can_be_infected(self.infection),
                neighbours
            )
        )
        for neighbour in can_be_infected_neighbours:
            if ProbabilityService.random_percentage(self.infection.infection_probability):
                neighbour.set_infected(self.infection)

    def get_neighbors(self):
        neighbours = GridService.get_grid_content(
            grid=self.model.grid,
            positions=GridService.get_agent_neighbour_position(
                agent=self
            )
        )
        return neighbours

    def can_be_infected(self, infection):
        return self.infection_state == InfectionState.HEALTHY and not self.is_immune(infection)

    def set_infected(self, infection):
        if not self.can_be_infected(infection):
            raise InfectionException()
        self.infection_state = InfectionState.INFECTED
        self.infection = infection

    def is_infected(self):
        return self.infection_state == InfectionState.INFECTED

    def is_healthy(self):
        return self.infection_state == InfectionState.HEALTHY

    def is_immune(self, infection):
        return infection.infection_id in self.immunity

    def is_unaware(self):
        return self.infection_knowledge_state == InfectionKnowledgeState.UNAWARE

    def is_aware(self):
        return self.infection_knowledge_state == InfectionKnowledgeState.AWARE

    def set_immune(self, infection):
        if self.infection_state != InfectionState.INFECTED:
            raise SystemError("A non infected agent cannot become immune")
        self.infection_state = InfectionState.HEALTHY
        if self.is_aware():
            self.infection_knowledge_state = InfectionKnowledgeState.UNAWARE
            self.lockdown = False
        if infection.infection_id not in self.immunity:
            self.immunity.append(infection.infection_id)

    def set_dead(self):
        if self.infection_state != InfectionState.INFECTED:
            raise SystemError("A non infected agent cannot die")
        self.infection_state = InfectionState.DEAD
        self.infection.infection_score += 10
        self.infection.victim_number += 1

        self.model.kill_human(agent=self)

    def set_aware(self):
        self.infection_knowledge_state = InfectionKnowledgeState.AWARE
        if self.is_infected():
            self.set_lockdown()

    def set_lockdown(self):
        self.lockdown = True

    def set_no_lockdown(self):
        self.lockdown = False

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
        if self.is_infected():
            data["Color"] = "red"
        if self.lockdown:
            data["Color"] = "blue"

        return data
