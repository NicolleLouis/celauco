from model.human_agents.base_human import BaseHuman
from model.non_human_agents.base_non_human import BaseNonHuman


class VaccinationCenter(BaseNonHuman):
    def __init__(self, unique_id, model, **kwargs):
        super().__init__(unique_id, model)
        self.grid = self.model.grid

        self.detection_range = 4
        self.known_infections = []
        self.vaccine_inoculated = 0

    def step(self):
        humans = self.get_human_inside_detection_range()
        for human in humans:
            self.analyse_infection(human)
            self.vaccine_human(human)

    def analyse_infection(self, human):
        if not human.is_infected():
            return
        infection = human.infection
        if infection not in self.known_infections:
            self.known_infections.append(infection)
            print("New infection discovered")

    def vaccine_human(self, human):
        for infection in self.known_infections:
            vaccine_result = human.set_immune(infection=infection)
            if vaccine_result:
                self.vaccine_inoculated += 1
                print(self.vaccine_inoculated)

    def get_human_inside_detection_range(self):
        agents_in_detection_range = self.grid.get_grid_content(
            positions=self.grid.get_agent_neighbour_position(
                agent=self,
                radius=self.detection_range
            )
        )
        humans_in_detection_range = list(
            filter(
                lambda agent: isinstance(agent, BaseHuman),
                agents_in_detection_range
            )
        )
        return humans_in_detection_range

    def is_in_grid(self):
        return True

    def display(self):
        data = {
            "Shape": "images/medic",
            "Layer": 1,
            "scale": 1,
        }

        return data
