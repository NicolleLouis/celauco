import random


class ProbabilityService:
    @staticmethod
    def random_probability(probability):
        return random.randint(0, 100) < probability
