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
            model_reporters["Hospital Occupancy"] = self.human_in_hospital

        if len(self.model.countries) == 2:
            model_reporters["Infected (Left)"] = self.number_infected_1
            model_reporters["Infected (Right)"] = self.number_infected_2
            model_reporters["Density (Left)"] = self.density_1
            model_reporters["Density (Right)"] = self.density_2

        if len(self.model.countries) == 1:
            model_reporters["Density"] = self.density

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

    def number_infected_1(self):
        if len(self.model.countries) != 2:
            raise Exception("This only works for 2 countries")
        country = self.model.countries[0]
        humans = self.model.get_all_humans(country)
        infected_humans = list(
            filter(
                lambda human: human.is_infected(),
                humans
            )
        )
        return len(infected_humans)

    def number_infected_2(self):
        if len(self.model.countries) != 2:
            raise Exception("This only works for 2 countries")
        country = self.model.countries[1]
        humans = self.model.get_all_humans(country)
        infected_humans = list(
            filter(
                lambda human: human.is_infected(),
                humans
            )
        )
        return len(infected_humans)

    def density_1(self):
        if len(self.model.countries) != 2:
            raise Exception("This only works for 2 countries")
        country = self.model.countries[0]
        return country.density

    def density_2(self):
        if len(self.model.countries) != 2:
            raise Exception("This only works for 2 countries")
        country = self.model.countries[1]
        return country.density

    def density(self):
        if len(self.model.countries) != 1:
            raise Exception("This only works for 1 countries")
        country = self.model.countries[0]
        return country.density

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
