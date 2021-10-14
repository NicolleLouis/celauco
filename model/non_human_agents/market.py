from model.human_agents.base_human import BaseHuman
from model.non_human_agents.base_non_human import BaseNonHuman
from service.grid import GridService
from service.movement import MovementService
from service.probability import ProbabilityService


class Market(BaseNonHuman):
    def __init__(self, *args):
        super().__init__(*args)
        self.detection_range = 5
        self.attraction_probability = 10

    def step(self):
        humans = self.get_human_inside_detection_range()
        for human in humans:
            if ProbabilityService.random_percentage(self.attraction_probability):
                self.attract_human(human)

    def get_human_inside_detection_range(self):
        agents_in_detection_range = GridService.get_grid_content(
            grid=self.model.grid,
            positions=GridService.get_agent_neighbour_position(
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

    def attract_human(self, human):
        if not human.can_be_moved(Market):
            return
        human.modify_position(
            MovementService.move_toward_agent(
                moving_agent=human,
                target_agent=self
            )
        )

    def is_in_grid(self):
        return True

    def display(self):
        data = {
            "Shape": "images/market",
            "Layer": 1,
            "scale": 1,
        }

        return data
