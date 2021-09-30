import random

from mesa import Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector

from exceptions.infection import InfectionException
from model.agents.base_agent import CelaucoAgent
from model.agents.medic import Medic
from model.agents.gilet_josne import GiletJosne


class CelaucoModel(Model):
    """A model with some number of agents."""
    def __init__(
            self,
            agents_number=20,
            medic_number=0,
            gilet_josne_number=0,
            initially_infected=1,
            width=10,
            height=10,
            infection_probability=25,
            infection_duration=10,
            death_probability=1,
    ):
        super().__init__()
        self.base_agent_number = agents_number

        self.medic_number = medic_number
        self.base_agent_number = self.base_agent_number - medic_number

        self.gilet_josne_number = gilet_josne_number
        self.base_agent_number = self.base_agent_number - gilet_josne_number

        self.schedule = RandomActivation(self)
        self.grid = MultiGrid(
            width=width,
            height=height,
            torus=False
        )
        self.running = True
        self.infection_probability = infection_probability
        self.infection_duration = infection_duration
        self.death_probability = death_probability
        self.number_of_dead = 0

        self.data_collector = DataCollector(
            model_reporters={
                "Healthy": self.number_healthy,
                "Infected": self.number_infected,
                "Immune": self.number_immune,
                "Dead": self.get_number_of_dead,
            },
        )

        # Create agents
        current_index = 0
        for index in range(self.base_agent_number):
            self.add_agent(agent_id=current_index)
            current_index += 1
        for index in range(self.medic_number):
            self.add_agent(agent_id=current_index, agent_class=Medic)
            current_index += 1
        for index in range(self.gilet_josne_number):
            self.add_agent(agent_id=current_index, agent_class=GiletJosne)
            current_index += 1

        self.infect_agent(number_of_agent_to_infect=initially_infected)

    def step(self):
        self.data_collector.collect(self)
        self.schedule.step()
        self.should_continue()

    def infect_agent(self, number_of_agent_to_infect):
        agents = self.schedule.agents
        if number_of_agent_to_infect > len(agents):
            raise SystemError("Cannot infect that much agents")
        for index in range(number_of_agent_to_infect):
            agent = random.choice(agents)
            try:
                agent.set_infected()
            except InfectionException:
                pass

    def add_agent(self, agent_id: object, agent_class: object = CelaucoAgent) -> object:
        agent = agent_class(agent_id, self)
        self.schedule.add(agent)

        x, y = self.get_random_position()
        self.grid.place_agent(agent, (x, y))

    def kill_agent(self, agent):
        self.schedule.remove(agent)
        self.grid.remove_agent(agent)
        self.number_of_dead += 1

    def get_random_position(self):
        x = self.random.randrange(self.grid.width)
        y = self.random.randrange(self.grid.height)
        return x, y

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

    def get_number_of_dead(self):
        return self.number_of_dead
