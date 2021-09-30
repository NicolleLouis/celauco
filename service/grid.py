class GridService:
    @staticmethod
    def get_neighbour_position(grid, position):
        neighbor_positions = grid.get_neighborhood(
            position,
            moore=True,
            include_center=True,
        )
        return neighbor_positions

    @staticmethod
    def get_grid_content(grid, positions):
        return grid.get_cell_list_contents(positions)
