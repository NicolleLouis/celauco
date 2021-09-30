from model.agents.base_agent import CelaucoAgent


class Medic(CelaucoAgent):
    def additional_step(self):
        neighbours = self.get_neighbors()
        infected_neighbours = list(
            filter(
                lambda neighbour: neighbour.is_infected(),
                neighbours
            )
        )
        unaware_neighbours = list(
            filter(
                lambda neighbour: neighbour.is_unaware(),
                infected_neighbours
            )
        )
        for neighbour in unaware_neighbours:
            neighbour.set_aware()

    def display(self):
        data = super().display()
        data["Shape"] = "rect"
        return data
