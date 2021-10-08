import random
import uuid

from constants.infection_name import animals, adjectives


class Infection:
    def __init__(
            self,
            infection_probability: int,
            infection_duration: int,
            death_probability: int,
    ):
        self.infection_id = uuid.uuid4()
        self.name = Infection.generate_infection_name()
        self.infection_probability = infection_probability
        self.infection_duration = infection_duration
        self.death_probability = death_probability
        self.co_immunity = []

    def add_co_immunity(self, other_infection):
        self.co_immunity.append(other_infection.infection_id)

    @staticmethod
    def generate_infection_name():
        animal = random.choice(animals)
        adjective = random.choice(adjectives)
        return '{animal} {adjective}'.format(
            animal=animal,
            adjective=adjective
        )
