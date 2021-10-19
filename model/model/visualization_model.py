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
            macron_starting_lockdown_minimal_ratio=10,
            macron_stopping_lockdown_minimal_ratio=5,
            macron_lockdown_severity=100,
            macron_starting_lockdown_minimal_ratio_1=10,
            macron_stopping_lockdown_minimal_ratio_1=5,
            macron_lockdown_severity_1=100,
            macron_starting_lockdown_minimal_ratio_2=10,
            macron_stopping_lockdown_minimal_ratio_2=5,
            macron_lockdown_severity_2=100,
            macron_shut_down_market=True,
            macron_shut_down_market_1=True,
            macron_shut_down_market_2=True,
            hospital_bed=50,
            businessman_flight_probability=5,
            countries_number=1,
            **kwargs
    ):
        macron_parameters = self.generate_macron_parameters(
            macron_starting_lockdown_minimal_ratio=macron_starting_lockdown_minimal_ratio,
            macron_stopping_lockdown_minimal_ratio=macron_stopping_lockdown_minimal_ratio,
            macron_lockdown_severity=macron_lockdown_severity,
            macron_starting_lockdown_minimal_ratio_1=macron_starting_lockdown_minimal_ratio_1,
            macron_stopping_lockdown_minimal_ratio_1=macron_stopping_lockdown_minimal_ratio_1,
            macron_lockdown_severity_1=macron_lockdown_severity_1,
            macron_starting_lockdown_minimal_ratio_2=macron_starting_lockdown_minimal_ratio_2,
            macron_stopping_lockdown_minimal_ratio_2=macron_stopping_lockdown_minimal_ratio_2,
            macron_lockdown_severity_2=macron_lockdown_severity_2,
            macron_shut_down_market=macron_shut_down_market,
            macron_shut_down_market_1=macron_shut_down_market_1,
            macron_shut_down_market_2=macron_shut_down_market_2,
            countries_number=countries_number,
        )
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
            countries_number=countries_number,
            macron_parameters=macron_parameters,
            hospital_parameters={
                "hospital_bed": hospital_bed,
            },
            businessman_parameters={
                "flight_probability": businessman_flight_probability,
            },

            **kwargs
        )

    @staticmethod
    def generate_macron_parameters(
            countries_number,
            macron_starting_lockdown_minimal_ratio,
            macron_stopping_lockdown_minimal_ratio,
            macron_lockdown_severity,
            macron_shut_down_market,
            macron_shut_down_market_1,
            macron_shut_down_market_2,
            macron_starting_lockdown_minimal_ratio_1,
            macron_stopping_lockdown_minimal_ratio_1,
            macron_lockdown_severity_1,
            macron_starting_lockdown_minimal_ratio_2,
            macron_stopping_lockdown_minimal_ratio_2,
            macron_lockdown_severity_2,
    ):
        if countries_number == 1:
            macron_parameters = {
                "starting_lockdown_minimal_ratio": macron_starting_lockdown_minimal_ratio,
                "stopping_lockdown_minimal_ratio": macron_stopping_lockdown_minimal_ratio,
                "lockdown_severity": macron_lockdown_severity,
                "shut_down_market": macron_shut_down_market,
            }
        elif countries_number == 2:
            macron_parameters = [
                {
                    "starting_lockdown_minimal_ratio": macron_starting_lockdown_minimal_ratio_1,
                    "stopping_lockdown_minimal_ratio": macron_stopping_lockdown_minimal_ratio_1,
                    "lockdown_severity": macron_lockdown_severity_1,
                    "shut_down_market": macron_shut_down_market_1,
                },
                {
                    "starting_lockdown_minimal_ratio": macron_starting_lockdown_minimal_ratio_2,
                    "stopping_lockdown_minimal_ratio": macron_stopping_lockdown_minimal_ratio_2,
                    "lockdown_severity": macron_lockdown_severity_2,
                    "shut_down_market": macron_shut_down_market_2,
                }
            ]
        return macron_parameters
