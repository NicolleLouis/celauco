from service.grid import GridService


class MovementService:
    @staticmethod
    def random_move(agent):
        new_position = agent.random.choice(agent.get_neighbour_positions())
        return new_position

    @staticmethod
    def avoid_agents(agent):
        best_positions = []
        minimum_agent_neighbours = 9
        for position in agent.get_neighbour_positions():
            number_of_agent_neighbours = len(
                GridService.get_grid_content(
                    grid=agent.model.grid,
                    positions=GridService.get_neighbour_position(
                        grid=agent.model.grid,
                        position=agent.pos
                    )
                )
            )
            if number_of_agent_neighbours == minimum_agent_neighbours:
                best_positions.append(position)
            if number_of_agent_neighbours < minimum_agent_neighbours:
                minimum_agent_neighbours = number_of_agent_neighbours
                best_positions = [position]
        return agent.random.choice(best_positions)
