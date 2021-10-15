from mesa import Agent


class BaseNonHuman(Agent):
    """
        Base Non Human class, function to override:
        - step()
        - is_in_grid()
        - display()
    """
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

    def step(self):
        pass

    def is_in_grid(self):
        raise NotImplementedError("Should explain if it's in grid or not")

    def display(self):
        raise NotImplementedError("Should detail its own display if needed")
