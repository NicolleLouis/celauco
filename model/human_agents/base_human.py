from mesa import Agent

from constants.player_state import InfectionState
from exceptions.infection import InfectionException
from service.infection_service import InfectionService
from service.movement import MovementService
from service.probability import ProbabilityService


class BaseHuman(Agent):
    """
    Base Human class, function to override:
    - move()
    - additional_step()
    - display()
    - can_be_moved()

    Signals:
    pre_death_callback:
        - list of function to run before death, see self.pre_death() function
        - Interact with the list with: self.add_pre_death_callback
    """

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.pre_death_callback = []

        self.infection = None
        self.infection_state = InfectionState.HEALTHY
        self.infection_duration = 0
        self.immunity = []

        self.lockdown = False
        self.lockdown_severity = 100

        self.grid = self.model.grid

    def step(self):
        self.move()
        self.additional_step()
        if self.is_infected():
            self.infect_neighbours()
            self.infection_mutation()
            self.infection_evolution()

    def move(self):
        new_position = self.next_position()
        self.modify_position(new_position)

    def modify_position(self, position):
        self.grid.move_agent(self, position)

    @staticmethod
    def can_be_moved(object_class):
        """
        Tells another instance if this instance can moves us based on its class.
        Default is True.
        :param object_class: the class of the object asking
        :return: True or False
        """
        return True

    def next_position(self):
        if self.lockdown and ProbabilityService.random_percentage(self.lockdown_severity):
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
        neighbors = self.grid.get_grid_content(
            positions=self.grid.get_agent_neighbour_position(
                agent=self
            )
        )
        neighbors = list(
            filter(
                lambda neighbor: isinstance(neighbor, BaseHuman),
                neighbors
            )
        )
        return neighbors

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

    def set_immune(self, infection):
        if self.infection_state != InfectionState.INFECTED:
            raise SystemError("A non infected agent cannot become immune")
        self.infection_state = InfectionState.HEALTHY
        if infection.infection_id not in self.immunity:
            self.immunity.append(infection.infection_id)

    def set_dead(self):
        if self.infection_state != InfectionState.INFECTED:
            raise SystemError("A non infected agent cannot die")

        should_continue = self.pre_death()
        if not should_continue:
            return

        self.remove_from_model()
        self.update_death_data()

    def remove_from_model(self):
        self.model.schedule.remove(self)
        self.grid.remove_agent(self)

    def update_death_data(self):
        self.infection_state = InfectionState.DEAD
        self.infection.infection_score += 10
        self.infection.victim_number += 1
        self.model.add_dead()

    def set_lockdown(self, lockdown_severity=100):
        self.lockdown = True
        self.lockdown_severity = lockdown_severity

    def set_no_lockdown(self):
        self.lockdown = False

    @staticmethod
    def is_in_scheduler():
        return True

    def add_pre_death_callback(self, pre_death_callback):
        if not hasattr(pre_death_callback, '__call__'):
            raise Exception("Callback must be a function")
        self.pre_death_callback.append(pre_death_callback)

    def pre_death(self):
        """
        Run all function inside self.pre_death_callback
        callback argument: agent=self
        If one of them return false stop the whole death process
        :return: False if death process should be stopped, True if it should continue
        """
        for callback in self.pre_death_callback:
            result = callback(agent=self)
            if not result:
                return False
        return True

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
