import uuid

from model.human_agents.base_human import BaseHuman
from model.human_agents.gilet_josne import GiletJosne
from model.non_human_agents.hospital import Hospital
from model.non_human_agents.macron import Macron
from model.non_human_agents.market import Market
from model.non_human_agents.wall import Wall
from model.human_agents.businessman import BusinessMan


class AgentGenerator:
    def __init__(self, model, schedule, grid):
        self.schedule = schedule
        self.grid = grid
        self.model = model

    @staticmethod
    def get_agent_parameters(agent_class, **kwargs):
        equivalent_class_parameters = {
            Macron: "macron_parameters",
            Hospital: "hospital_parameters",
            BusinessMan: "businessman_parameters",
        }

        if agent_class in equivalent_class_parameters:
            if equivalent_class_parameters[agent_class] in kwargs:
                return kwargs[equivalent_class_parameters[agent_class]]
        return None

    def initialise_agents(
            self,
            human_number,
            **kwargs
    ):
        agent_classes = {
            "gilet_josne_number": GiletJosne,
            "businessman_number": BusinessMan,
            "macron": Macron,
            "market_number": Market,
            "wall_positions": Wall,
            "hospital": Hospital,
        }

        custom_generation_function = {
            Macron: self.generate_macron
        }

        # Create agents
        self.add_agents_randomly(agents_number=human_number)
        for kwarg in kwargs:
            if kwarg in agent_classes:
                agent_class = agent_classes[kwarg]
                agent_parameters = self.get_agent_parameters(agent_class, **kwargs)

                if agent_class in custom_generation_function:
                    custom_generation_function[agent_class](agent_parameters)
                elif isinstance(kwargs[kwarg], int):
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
                    model=self.model,
                    **agent_parameters,
                )
            else:
                agent = agent_class(
                    unique_id=uuid.uuid4(),
                    model=self.model,
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
                    model=self.model,
                    **agent_parameters,
                )
            else:
                agent = agent_class(
                    unique_id=uuid.uuid4(),
                    model=self.model,
                )
            self.schedule.add(agent)
            self.grid.place_agent(agent, position)

    def generate_macron(self, macron_parameters):
        if isinstance(macron_parameters, list):
            for index, macron_parameter in enumerate(macron_parameters):
                macron_parameter["country"] = self.model.countries[index]
                self.add_agents_randomly(
                    agents_number=1,
                    agent_class=Macron,
                    agent_parameters=macron_parameter
                )
        else:
            self.add_agents_randomly(
                agents_number=1,
                agent_class=Macron,
                agent_parameters=macron_parameters
            )
