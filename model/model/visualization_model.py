from model.model.model import CelaucoModel


class VisualizationModel(CelaucoModel):
    def __init__(
            self,
            width,
            height,
            human_number=20,
            initially_infected=1,
            infection_probability=10,
            infection_duration=30,
            death_probability=1,
            mutation_probability=0,
            verbose=False,
            maximum_number_of_turn=500,
            country_number=1,
            macron_starting_lockdown_minimal_ratio=0.1,
            macron_stopping_lockdown_minimal_ratio=2,
            macron_lockdown_severity=100,
            macron_shut_down_market=True,
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
                "starting_lockdown_minimal_ratio": macron_starting_lockdown_minimal_ratio,
                "stopping_lockdown_minimal_ratio": macron_stopping_lockdown_minimal_ratio,
                "lockdown_severity": macron_lockdown_severity,
                "shut_down_market": macron_shut_down_market,
            },
            **kwargs
        )
