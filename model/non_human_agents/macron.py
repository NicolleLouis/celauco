from model.non_human_agents.base_non_human import BaseNonHuman
from model.non_human_agents.market import Market


class Macron(BaseNonHuman):
    def __init__(
            self,
            unique_id,
            model,
            starting_lockdown_minimal_ratio=10,
            stopping_lockdown_minimal_ratio=5,
            lockdown_severity=100,
            shut_down_market=True,
            country=None,
    ):
        super().__init__(unique_id, model)
        self.is_global_lockdown = False

        self.starting_lockdown_minimal_ratio = starting_lockdown_minimal_ratio
        self.stopping_lockdown_minimal_ratio = stopping_lockdown_minimal_ratio
        self.lockdown_severity = lockdown_severity
        self.shut_down_market = shut_down_market
        self.country = country

    def step(self):
        infection_ratio = self.get_global_infection_state()
        if self.is_global_lockdown:
            if infection_ratio < self.stopping_lockdown_minimal_ratio:
                self.stop_global_lockdown()
        if not self.is_global_lockdown:
            if infection_ratio > self.starting_lockdown_minimal_ratio:
                self.start_global_lockdown()

    def get_all_humans(self):
        if self.country is not None:
            return self.model.get_all_humans(country=self.country)
        self.model.get_all_humans()

    def get_global_infection_state(self):
        humans = self.get_all_humans()
        humans_number = len(humans)
        infected_number = len(
            list(
                filter(
                    lambda human: human.is_infected(),
                    humans
                )
            )
        )
        return 100 * (infected_number / humans_number)

    def start_global_lockdown(self):
        if self.is_global_lockdown:
            return
        self.start_human_lockdown()
        self.close_all_market()

        self.is_global_lockdown = True

    def stop_global_lockdown(self):
        if not self.is_global_lockdown:
            return
        self.stop_human_lockdown()

        markets = self.get_all_market()
        for market in markets:
            market.set_open()

        self.is_global_lockdown = False

    def start_human_lockdown(self):
        humans = self.get_all_humans()
        for human in humans:
            human.set_lockdown(lockdown_severity=self.lockdown_severity)

    def stop_human_lockdown(self):
        if not self.is_global_lockdown:
            return
        humans = self.get_all_humans()
        for human in humans:
            human.set_no_lockdown()

    def close_all_market(self):
        if not self.shut_down_market:
            return
        markets = self.get_all_market()
        for market in markets:
            market.set_closed()

    def open_all_market(self):
        if not self.shut_down_market:
            return
        markets = self.get_all_market()
        for market in markets:
            market.set_open()

    def get_all_market(self):
        return self.model.get_all_agent_of_class(Market, country=self.country)

    def is_in_grid(self):
        return False

    def display(self):
        return {}
