import random
import uuid

from mesa import Model
from mesa.time import RandomActivation

from exceptions.infection import InfectionException
from model.human_agents.base_human import BaseHuman
from model.infection import Infection
from model.model.grid import Grid
from model.model.model_data_collector import ModelDataCollector
from service.geographic_service import GeographicService


class CelaucoModel(Model):
    """A model with some number of agents."""

    def __init__(
            self,
            width,
            height,
            human_number=20,
            initially_infected=1,
            infection_probability=10,
            infection_duration=30,
            death_probability=0,
            mutation_probability=0,
            verbose=False,
            maximum_number_of_turn=500,
            country_number=1,
            **kwargs
    ):
        """
        :param kwargs:
        Human Parameters:
            - gilet_josne_number: int
            - businessman_number: int
        Non Human Parameters:
            - macron: bool
            - market_number: int
            - wall_positions: list(pos)
            - hospital: bool
        Log paramaters:
            - log_variant_info: default = True
        """
        super().__init__()

        self.schedule = RandomActivation(self)
        self.grid = Grid(
            width=width,
            height=height,
        )
        self.countries = GeographicService(
            width=width,
            height=height
        ).generate_countries(
            country_number=country_number
        )
        self.running = True
        self.turn_number = 0
        self.maximum_number_of_turn = maximum_number_of_turn

        self.infection = Infection(
            infection_probability=infection_probability,
            infection_duration=infection_duration,
            death_probability=death_probability,
            mutation_probability=mutation_probability,
        )
        self.number_of_dead = 0
        self.known_infections = [self.infection]

        if "log_variant_info" in kwargs:
            self.log_variant_info = kwargs["log_variant_info"]
        else:
            self.log_variant_info = True
        self.verbose = verbose
        self.initialise_agents(
            initially_infected=initially_infected,
            human_number=human_number,
            **kwargs
        )
        self.setup_graph_collector()

    def step(self):
        self.graph_collector.collect(self)
        if self.log_variant_info:
            self.variant_collector.collect(self)
        self.schedule.step()
        self.turn_number += 1
        self.should_continue()
        if not self.running:
            self.end_step()
        self.infection.display()

    def end_step(self):
        if self.verbose:
            print('######')
            print("number of dead: {}".format(self.number_of_dead))
            self.display_biggest_infections()

    def infect_agent(self, number_of_agent_to_infect):
        humans = self.get_all_humans()
        if number_of_agent_to_infect > len(humans):
            raise SystemError("Cannot infect that much agents")
        for index in range(number_of_agent_to_infect):
            human = random.choice(humans)
            try:
                human.set_infected(self.infection)
            except InfectionException:
                pass

    def add_agents_randomly(
            self,
            agents_number,
            agent_class=BaseHuman,
            agent_parameters=None,
    ):
        for _i in range(agents_number):
            if agent_parameters is not None:
                agent = agent_class(
                    unique_id=uuid.uuid4(),
                    model=self,
                    **agent_parameters,
                )
            else:
                agent = agent_class(
                    unique_id=uuid.uuid4(),
                    model=self,
                )
            self.schedule.add(agent)

            if isinstance(agent, BaseHuman) or agent.is_in_grid():
                self.grid.place_agent_randomly(agent)

    def add_agents_in_position(
            self,
            agent_class,
            positions,
            agent_parameters=None,
    ):
        for position in positions:
            if agent_parameters is not None:
                agent = agent_class(
                    unique_id=uuid.uuid4(),
                    model=self,
                    **agent_parameters,
                )
            else:
                agent = agent_class(
                    unique_id=uuid.uuid4(),
                    model=self,
                )
            self.schedule.add(agent)
            self.grid.place_agent(agent, position)

    def add_dead(self):
        self.number_of_dead += 1

    def add_known_infection(self, infection):
        self.known_infections.append(infection)

    def get_biggest_infections(self):
        sorted_infections = sorted(
            self.known_infections,
            key=lambda infection: infection.infection_score,
            reverse=True,
        )
        return sorted_infections[:5]

    def display_biggest_infections(self):
        biggest_infection = self.get_biggest_infections()
        for infection in biggest_infection:
            infection.display()

    def get_biggest_infections_name(self):
        biggest_infection_name = list(
            map(
                lambda infection: infection.name,
                self.get_biggest_infections()
            )
        )
        return biggest_infection_name

    def should_continue(self):
        if self.turn_number > self.maximum_number_of_turn:
            self.running = False
            return
        humans = self.get_all_humans()
        infected_humans = list(
            filter(
                lambda human: human.is_infected(),
                humans
            )
        )
        self.running = len(infected_humans) > 0

    def get_all_humans(self):
        return self.get_all_agent_of_class(BaseHuman)

    def get_all_agent_of_class(self, agent_class):
        agents = self.schedule.agents
        filtered_agents = list(
            filter(
                lambda agent: isinstance(agent, agent_class),
                agents
            )
        )
        return filtered_agents

    def setup_graph_collector(self):
        self.data_collector = ModelDataCollector(model=self)
        self.graph_collector = self.data_collector.generate_graph_collector()
        if self.log_variant_info:
            self.variant_collector = self.data_collector.generate_variant_collector()

    def get_agent_parameters(self, agent_class, **kwargs):
        from model.non_human_agents.macron import Macron

        equivalent_class_parameters = {
            Macron: "macron_parameters"
        }

        if agent_class in equivalent_class_parameters:
            if equivalent_class_parameters[agent_class] in kwargs:
                return kwargs[equivalent_class_parameters[agent_class]]
        return None

    def initialise_agents(
            self,
            human_number,
            initially_infected,
            **kwargs
    ):
        from model.human_agents.businessman import BusinessMan
        from model.human_agents.gilet_josne import GiletJosne
        from model.non_human_agents.hospital import Hospital
        from model.non_human_agents.macron import Macron
        from model.non_human_agents.market import Market
        from model.non_human_agents.wall import Wall

        agent_classes = {
            "gilet_josne_number": GiletJosne,
            "businessman_number": BusinessMan,
            "macron": Macron,
            "market_number": Market,
            "wall_positions": Wall,
            "hospital": Hospital,
        }

        # Create agents
        self.add_agents_randomly(agents_number=human_number)
        for kwarg in kwargs:
            if kwarg in agent_classes:
                agent_class = agent_classes[kwarg]
                agent_parameters = self.get_agent_parameters(agent_class, **kwargs)

                if isinstance(kwargs[kwarg], int):
                    agents_number = kwargs[kwarg]
                    self.add_agents_randomly(
                        agents_number=agents_number,
                        agent_class=agent_class,
                        agent_parameters=agent_parameters,
                    )
                elif isinstance(kwargs[kwarg], bool):
                    if kwargs[kwarg]:
                        agents_number = 1
                        self.add_agents_randomly(
                            agents_number=agents_number,
                            agent_class=agent_class,
                            agent_parameters=agent_parameters,
                        )
                elif isinstance(kwargs[kwarg], list):
                    self.add_agents_in_position(
                        agent_class=agent_class,
                        positions=kwargs[kwarg],
                        agent_parameters=agent_parameters,
                    )
                else:
                    raise Exception('Agent number must be a int or a bool')

        self.infect_agent(number_of_agent_to_infect=initially_infected)
