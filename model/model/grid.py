import random
from mesa.space import MultiGrid

from model.non_human_agents.wall import Wall


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
        self.wall_positions = []

    def place_agent_randomly(self, agent):
        random_position = self.get_random_position()
        self.place_agent(agent, random_position)

    def place_agent(self, agent, position) -> None:
        if isinstance(agent, Wall):
            self.wall_positions.append(position)

        super(Grid, self).place_agent(
            agent=agent,
            pos=position
        )

    def is_position_valid(self, position):
        if position in self.wall_positions:
            return False
        return True

    def get_agent_valid_neighbour_position(self, agent, radius=1):
        agent_position = agent.pos
        neighbour_position = self.get_neighbour_position(
            position=agent_position,
            radius=radius
        )
        neighbour_valid_position = list(
            filter(
                lambda position: self.is_position_valid(position=position),
                neighbour_position
            )
        )
        return neighbour_valid_position

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
