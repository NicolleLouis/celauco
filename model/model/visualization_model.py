from model.model.model import CelaucoModel


class VisualizationModel(CelaucoModel):
    def __init__(
            self,
            human_number=20,
            initially_infected=1,
            width=10,
            height=10,
            infection_probability=25,
            infection_duration=10,
            death_probability=5,
            mutation_probability=5,
            verbose=False,
            maximum_number_of_turn=500,
            country_number=1,
            macron_starting_lockdown_minimal_ratio=0.1,
            **kwargs
    ):
        super().__init__(
            human_number=human_number,
            initially_infected=initially_infected,
            width=width,
            height=height,
            infection_probability=infection_probability,
            infection_duration=infection_duration,
            death_probability=death_probability,
            mutation_probability=mutation_probability,
            verbose=verbose,
            maximum_number_of_turn=maximum_number_of_turn,
            country_number=country_number,
            macron_parameters={
                "starting_lockdown_minimal_ratio": macron_starting_lockdown_minimal_ratio
            },
            **kwargs
        )
