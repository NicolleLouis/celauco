import random

from mesa import Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector

from exceptions.infection import InfectionException
from model.agents.base_agent import CelaucoAgent
from model.agents.businessman import BusinessMan
from model.agents.medic import Medic
from model.agents.gilet_josne import GiletJosne
from model.infection import Infection
from service.grid import GridService


class CelaucoModel(Model):
    """A model with some number of agents."""
    def __init__(
            self,
            human_number=20,
            medic_number=0,
            gilet_josne_number=0,
            businessman_number=0,
            initially_infected=1,
            width=10,
            height=10,
            infection_probability=25,
            infection_duration=10,
            death_probability=5,
    ):
        super().__init__()
        self.human_number = human_number
        self.medic_number = medic_number
        self.gilet_josne_number = gilet_josne_number
        self.businessman_number = businessman_number

        self.schedule = RandomActivation(self)
        self.grid = MultiGrid(
            width=width,
            height=height,
            torus=False
        )
        self.running = True
        self.infection = Infection(
            infection_probability=infection_probability,
            infection_duration=infection_duration,
            death_probability=death_probability,
        )
        self.number_of_dead = 0

        self.graph_collector = DataCollector(
            model_reporters={
                "Healthy": self.number_healthy,
                "Infected": self.number_infected,
                "Immune": self.number_immune,
                "Dead": self.number_dead,
            },
        )
        self.variant_collector = DataCollector(
            model_reporters={
                "Variant": self.compute_compex_data,
            },
        )

        # Create agents
        current_index = 0
        for index in range(self.human_number):
            self.add_agent(agent_id=current_index)
            current_index += 1
        for index in range(self.medic_number):
            self.add_agent(agent_id=current_index, agent_class=Medic)
            current_index += 1
        for index in range(self.gilet_josne_number):
            self.add_agent(agent_id=current_index, agent_class=GiletJosne)
            current_index += 1
        for index in range(self.businessman_number):
            self.add_agent(agent_id=current_index, agent_class=BusinessMan)
            current_index += 1

        self.infect_agent(number_of_agent_to_infect=initially_infected)

    def step(self):
        self.graph_collector.collect(self)
        self.variant_collector.collect(self)
        self.schedule.step()
        self.should_continue()

    def infect_agent(self, number_of_agent_to_infect):
        agents = self.schedule.agents
        if number_of_agent_to_infect > len(agents):
            raise SystemError("Cannot infect that much agents")
        for index in range(number_of_agent_to_infect):
            agent = random.choice(agents)
            try:
                agent.set_infected(self.infection)
            except InfectionException:
                pass

    def add_agent(self, agent_id, agent_class=CelaucoAgent):
        agent = agent_class(agent_id, self)
        self.schedule.add(agent)

        x, y = GridService.get_random_position(self.grid)
        self.grid.place_agent(agent, (x, y))

    def kill_agent(self, agent):
        self.schedule.remove(agent)
        self.grid.remove_agent(agent)
        self.number_of_dead += 1

    def should_continue(self):
        agents = self.schedule.agents
        infected_agents = list(
            filter(
                lambda agent: agent.is_infected(),
                agents
            )
        )
        self.running = len(infected_agents) > 0

    def number_healthy(self):
        agents = self.schedule.agents
        healthy_agents = list(
            filter(
                lambda agent: agent.is_healthy(),
                agents
            )
        )
        return len(healthy_agents)

    def number_infected(self):
        agents = self.schedule.agents
        infected_agents = list(
            filter(
                lambda agent: agent.is_infected(),
                agents
            )
        )
        return len(infected_agents)

    def number_immune(self):
        agents = self.schedule.agents
        immune_agents = list(
            filter(
                lambda agent: agent.is_immune(),
                agents
            )
        )
        return len(immune_agents)

    def number_dead(self):
        return self.number_of_dead

    def compute_compex_data(self):
        # ToDo: compute real variant data #
        return [
            {
                'variant_name': "test",
                'infected_number': 12
            }
        ]
