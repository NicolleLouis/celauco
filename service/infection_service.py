import random

from model.infection import Infection


class InfectionService:
    @classmethod
    def generate_random_infection(cls):
        infection_probability = random.randint(0, 100)
        infection_duration = random.randint(0, 50)
        death_probability = random.randint(0, 100)
        mutation_probability = random.randint(0, 100)
        return Infection(
            infection_probability=infection_probability,
            infection_duration=infection_duration,
            death_probability=death_probability,
            mutation_probability=mutation_probability,
        )

    @classmethod
    def generate_infection(cls, infection):
        infection_probability = random.randint(0, 100)
        death_probability = random.randint(0, 100)
        mutation_probability = random.randint(0, 100)
        return Infection(
            infection_duration=infection.infection_duration,
            infection_probability=infection_probability,
            death_probability=death_probability,
            mutation_probability=mutation_probability,
        )
