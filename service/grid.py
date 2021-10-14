import random


class GridService:
    @staticmethod
    def get_agent_neighbour_position(agent, radius=1):
        return GridService.get_neighbour_position(
            grid=agent.model.grid,
            position=agent.pos,
            radius=radius
        )

    @staticmethod
    def get_neighbour_position(grid, position, radius=1):
        neighbor_positions = grid.get_neighborhood(
            position,
            moore=True,
            include_center=True,
            radius=radius,
        )
        return neighbor_positions

    @staticmethod
    def get_grid_content(grid, positions):
        return grid.get_cell_list_contents(positions)

    @staticmethod
    def get_random_position(grid):
        x = random.randrange(grid.width)
        y = random.randrange(grid.height)
        return x, y
