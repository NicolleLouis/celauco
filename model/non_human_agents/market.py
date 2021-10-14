from model.non_human_agents.base_non_human import BaseNonHuman


class Market(BaseNonHuman):
    def step(self):
        pass

    def is_in_grid(self):
        return True

    def display(self):
        data = {
            "Shape": "market",
            "Layer": 1,
            "r": 0.5,
            "w": 0.5,
            "h": 0.5,
        }
        return data
