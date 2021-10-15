from model.non_human_agents.base_non_human import BaseNonHuman


class Wall(BaseNonHuman):
    def __init__(self, *args):
        super().__init__(*args)

    def is_in_grid(self):
        return True

    def display(self):
        data = {
            "Shape": "rect",
            "Layer": 2,
            "w": 0.9,
            "h": 1,
            "Color": "grey",
            "Filled": True,
        }

        return data
