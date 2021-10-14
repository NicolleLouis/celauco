import random

from mesa import Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector

from exceptions.infection import InfectionException
from model.human_agents.base_human import BaseHuman
from model.human_agents.businessman import BusinessMan
from model.human_agents.gilet_josne import GiletJosne
from model.human_agents.medic import Medic
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
            mutation_probability=5,
            verbose=False,
    ):
        super().__init__()
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
            mutation_probability=mutation_probability,
        )
        self.number_of_dead = 0
        self.known_infections = [self.infection]

        self.graph_collector = DataCollector(
            model_reporters={
                "Healthy": self.number_healthy,
                "Infected": self.number_infected,
                "Dead": self.number_dead,
            },
        )
        self.variant_collector = DataCollector(
            model_reporters={
                "variant_data": self.compute_variant_data,
            },
        )

        self.verbose = verbose

        self.initialise_agents(
            initially_infected=initially_infected,
            human_number=human_number,
            medic_number=medic_number,
            gilet_josne_number=gilet_josne_number,
            businessman_number=businessman_number,
        )

    def step(self):
        self.graph_collector.collect(self)
        self.variant_collector.collect(self)
        self.schedule.step()
        self.should_continue()
        if not self.running:
            self.end_step()

    def end_step(self):
        if self.verbose:
            print('######')
            print("number of dead: {}".format(self.number_of_dead))
            self.display_biggest_infections()

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

    def add_agent(self, agent_id, agent_class=BaseHuman):
        agent = agent_class(agent_id, self)
        self.schedule.add(agent)

        x, y = GridService.get_random_position(self.grid)
        self.grid.place_agent(agent, (x, y))

    def kill_human(self, agent):
        if not agent.is_human():
            raise Exception("Should only kill humans")
        self.schedule.remove(agent)
        self.grid.remove_agent(agent)
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
        humans = self.get_all_humans()
        infected_humans = list(
            filter(
                lambda human: human.is_infected(),
                humans
            )
        )
        self.running = len(infected_humans) > 0

    def number_healthy(self):
        humans = self.get_all_humans()
        healthy_humans = list(
            filter(
                lambda human: human.is_healthy(),
                humans
            )
        )
        return len(healthy_humans)

    def number_infected(self):
        humans = self.get_all_humans()
        infected_humans = list(
            filter(
                lambda human: human.is_infected(),
                humans
            )
        )
        return len(infected_humans)

    def number_dead(self):
        return self.number_of_dead

    def get_all_humans(self):
        agents = self.schedule.agents
        humans = list(
            filter(
                lambda agent: agent.is_human(),
                agents
            )
        )
        return humans

    def compute_variant_data(self):
        agents = self.schedule.agents
        variant_data = {}
        infected_agents = filter(
            lambda agent: agent.is_infected(),
            agents
        )
        for agent in infected_agents:
            infection_name = agent.infection.name
            if infection_name in variant_data:
                variant_data[infection_name] += 1
            else:
                variant_data[infection_name] = 1
        return variant_data

    def initialise_agents(
            self,
            human_number,
            initially_infected,
            medic_number,
            gilet_josne_number,
            businessman_number,
    ):
        # Create agents
        current_index = 0
        for index in range(human_number):
            self.add_agent(agent_id=current_index)
            current_index += 1
        for index in range(medic_number):
            self.add_agent(agent_id=current_index, agent_class=Medic)
            current_index += 1
        for index in range(gilet_josne_number):
            self.add_agent(agent_id=current_index, agent_class=GiletJosne)
            current_index += 1
        for index in range(businessman_number):
            self.add_agent(agent_id=current_index, agent_class=BusinessMan)
            current_index += 1

        self.infect_agent(number_of_agent_to_infect=initially_infected)
