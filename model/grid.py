import random
from mesa.space import MultiGrid


class Grid(MultiGrid):
    def __init__(
            self,
            width,
            height,
    ):
        super().__init__(
            width=width,
            height=height,
            torus=False,
        )

    def place_agent_randomly(self, agent):
        random_position = self.get_random_position()
        self.place_agent(agent, random_position)

    def get_agent_neighbour_position(self, agent, radius=1):
        return self.get_neighbour_position(
            position=agent.pos,
            radius=radius
        )

    def get_neighbour_position(self, position, radius=1):
        neighbor_positions = self.get_neighborhood(
            position,
            moore=True,
            include_center=True,
            radius=radius,
        )
        return neighbor_positions

    def get_grid_content(self, positions):
        return self.get_cell_list_contents(positions)

    def get_random_position(self):
        x = random.randrange(self.width)
        y = random.randrange(self.height)
        return x, y
