import random
import uuid

from constants.infection_name import animals, adjectives


class Infection:
    def __init__(
            self,
            infection_probability: int,
            infection_duration: int,
            death_probability: int,
            mutation_probability: int,
    ):
        self.infection_id = uuid.uuid4()
        self.name = Infection.generate_infection_name()
        self.infection_probability = infection_probability
        self.infection_duration = infection_duration
        self.death_probability = death_probability
        self.mutation_probability = mutation_probability
        self.infection_score = 0
        self.victim_number = 0

    @staticmethod
    def generate_infection_name():
        animal = random.choice(animals)
        adjective = random.choice(adjectives)
        return '{animal} {adjective}'.format(
            animal=animal,
            adjective=adjective
        )

    def display(self):
        print("#####")
        print("Infection name: {}".format(self.name))
        print("Infection probability: {}".format(self.infection_probability))
        print("Infection duration: {}".format(self.infection_duration))
        print("Death probability: {}".format(self.death_probability))
        print("Mutation probability: {}".format(self.mutation_probability))
        print("Score: {}".format(self.infection_score))
        print("Victim number: {}".format(self.victim_number))
        print("#####")
