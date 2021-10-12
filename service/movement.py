from service.grid import GridService


class MovementService:
    @staticmethod
    def random_neighbours(agent):
        new_position = agent.random.choice(
            GridService.get_agent_neighbour_position(
                agent=agent
            )
        )
        return new_position

    @staticmethod
    def avoid_agents(agent):
        best_positions = [agent.pos]
        minimum_agent_neighbours = 9
        for position in GridService.get_agent_neighbour_position(
                agent=agent
        ):
            number_of_agent_neighbours = len(
                GridService.get_grid_content(
                    grid=agent.model.grid,
                    positions=GridService.get_neighbour_position(
                        grid=agent.model.grid,
                        position=position
                    )
                )
            )
            if number_of_agent_neighbours == minimum_agent_neighbours:
                best_positions.append(position)
            if number_of_agent_neighbours < minimum_agent_neighbours:
                minimum_agent_neighbours = number_of_agent_neighbours
                best_positions = [position]
        return agent.random.choice(best_positions)

    @staticmethod
    def search_agents(agent):
        best_positions = []
        maximum_agent_neighbours = 0
        for position in GridService.get_agent_neighbour_position(
                agent=agent
        ):
            number_of_agent_neighbours = len(
                GridService.get_grid_content(
                    grid=agent.model.grid,
                    positions=GridService.get_neighbour_position(
                        grid=agent.model.grid,
                        position=position
                    )
                )
            )
            if number_of_agent_neighbours == maximum_agent_neighbours:
                best_positions.append(position)
            if number_of_agent_neighbours > maximum_agent_neighbours:
                maximum_agent_neighbours = number_of_agent_neighbours
                best_positions = [position]
        return agent.random.choice(best_positions)

    @staticmethod
    def random_position(agent):
        new_position = GridService.get_random_position(agent.model.grid)
        return new_position
