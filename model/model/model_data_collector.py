from mesa.datacollection import DataCollector

from model.non_human_agents.hospital import Hospital


class ModelDataCollector:
    def __init__(self, model):
        self.model = model

    def generate_graph_collector(self):
        model_reporters = {
                "Healthy": self.number_healthy,
                "Infected": self.number_infected,
                "Dead": self.number_dead,
            }
        if len(self.model.get_all_agent_of_class(Hospital)) > 0:
            model_reporters["Human in Hospital"] = self.human_in_hospital

        return DataCollector(
            model_reporters=model_reporters,
        )

    def generate_variant_collector(self):
        return DataCollector(
            model_reporters={
                "variant_data": self.compute_variant_data,
            },
        )

    def number_dead(self):
        return self.model.number_of_dead

    def number_infected(self):
        humans = self.model.get_all_humans()
        infected_humans = list(
            filter(
                lambda human: human.is_infected(),
                humans
            )
        )
        return len(infected_humans)

    def number_healthy(self):
        humans = self.model.get_all_humans()
        healthy_humans = list(
            filter(
                lambda human: human.is_healthy(),
                humans
            )
        )
        return len(healthy_humans)

    def human_in_hospital(self):
        hospital = self.model.get_all_agent_of_class(Hospital)[0]
        return hospital.get_number_of_human_in_hospital()

    def compute_variant_data(self):
        humans = self.model.get_all_humans()
        variant_data = {}
        infected_agents = filter(
            lambda human: human.is_infected(),
            humans
        )
        for infected_human in infected_agents:
            infection_name = infected_human.infection.name
            if infection_name in variant_data:
                variant_data[infection_name] += 1
            else:
                variant_data[infection_name] = 1
        return variant_data
