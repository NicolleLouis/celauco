from model.non_human_agents.base_non_human import BaseNonHuman


class Macron(BaseNonHuman):
    def __init__(self, *args):
        super().__init__(*args)
        self.starting_lockdown_minimal_ratio = 0.25
        self.stopping_lockdown_minimal_ratio = 0.05
        self.is_global_lockdown = False

    def step(self):
        infection_ratio = self.get_global_infection_state()
        if self.is_global_lockdown:
            if infection_ratio < self.stopping_lockdown_minimal_ratio:
                self.stop_global_lockdown()
        if not self.is_global_lockdown:
            if infection_ratio > self.starting_lockdown_minimal_ratio:
                self.start_global_lockdown()

    def get_global_infection_state(self):
        humans_number = len(self.get_all_humans())
        infected_number = self.model.number_infected()
        return infected_number/humans_number

    def start_global_lockdown(self):
        if not self.is_global_lockdown:
            humans = self.get_all_humans()
            for human in humans:
                human.set_lockdown()
            self.is_global_lockdown = True

    def stop_global_lockdown(self):
        if self.is_global_lockdown:
            humans = self.get_all_humans()
            for human in humans:
                human.set_no_lockdown()
            self.is_global_lockdown = False

    def get_all_humans(self):
        return self.model.get_all_humans()

    def is_in_grid(self):
        return False

    def display(self):
        pass
