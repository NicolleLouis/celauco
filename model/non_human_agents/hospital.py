from model.non_human_agents.base_non_human import BaseNonHuman
from service.probability import ProbabilityService


class Hospital(BaseNonHuman):
    def __init__(self, unique_id, model, hospital_bed=50):
        super().__init__(unique_id, model)
        self.add_hospital_callback_to_all_human()
        self.agents_in_hospital = []

        self.hospital_bed = hospital_bed

    def add_hospital_callback_to_all_human(self):
        humans = self.model.get_all_humans()
        for human in humans:
            human.add_pre_death_callback(
                pre_death_callback=self.human_pre_death_callback
            )

    def step(self):
        for agent in self.agents_in_hospital:
            agent["agent"].infection_mutation()
            self.agent_infection_evolution(agent=agent)

    def agent_infection_evolution(self, agent):
        raw_agent = agent["agent"]
        raw_agent.infection_duration += 1
        raw_agent.infection.infection_score += 1
        # Immunity
        if raw_agent.infection_duration >= raw_agent.infection.infection_duration:
            raw_agent.set_cured()
            self.leave_hospital_immune(agent=agent)

        # Death
        else:
            if ProbabilityService.random_probability_1000(raw_agent.infection.death_probability):
                self.hospital_death(agent=agent)

    def leave_hospital_immune(self, agent):
        self.model.schedule.add(agent["agent"])
        self.model.grid.place_agent(agent["agent"], agent["position"])
        self.agents_in_hospital.remove(agent)

    def hospital_death(self, agent):
        agent["agent"].update_death_data()
        self.agents_in_hospital.remove(agent)

    def remove_from_hospital(self, agent):
        self.agents_in_hospital.remove(agent)

    def get_number_of_human_in_hospital(self):
        return len(self.agents_in_hospital)

    def human_pre_death_callback(self, agent):
        if len(self.agents_in_hospital) < self.hospital_bed:
            self.agents_in_hospital.append(
                {
                    "agent": agent,
                    "position": agent.pos,
                }
            )
            agent.remove_from_model()
            return False
        return True

    def is_in_grid(self):
        return False

    def display(self):
        return {}
