from model.agents.base_agent import CelaucoAgent
from service.movement import MovementService


class Medic(CelaucoAgent):
    def additional_step(self):
        self.tell_agent_about_infection()

    def next_position(self):
        if self.is_infected() and self.is_aware():
            new_position = MovementService.avoid_agents(agent=self)
        else:
            new_position = MovementService.search_agents(agent=self)
        return new_position

    def tell_agent_about_infection(self):
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
        data["Shape"] = "images/medic"
        data["scale"] = 0.5
        data["Layer"] = 1
        return data
