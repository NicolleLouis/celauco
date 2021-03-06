from mesa.visualization.UserParam import UserSettableParameter


class SliderService:
    @staticmethod
    def get_sliders(size):
        human_number = UserSettableParameter(
            param_type="slider",
            name="Human number",
            value=int(size * size / 5),
            min_value=0,
            max_value=size * size,
        )
        businessman_number = UserSettableParameter(
            param_type="slider",
            name="BusinessMan number",
            value=0,
            min_value=0,
            max_value=size * size,
        )
        gilet_josne_number = UserSettableParameter(
            param_type="slider",
            name="Party Monsters number",
            value=0,
            min_value=0,
            max_value=size * size,
        )
        infection_probability = UserSettableParameter(
            param_type="slider",
            name="Infection probability",
            value=10,
            min_value=0,
            max_value=100,
        )
        infection_duration = UserSettableParameter(
            param_type="slider",
            name="Infection duration",
            value=30,
            min_value=1,
            max_value=50,
        )
        death_probability = UserSettableParameter(
            param_type="slider",
            name="Death probabity (*0.1)",
            value=1,
            min_value=0,
            max_value=100,
        )
        mutation_probability = UserSettableParameter(
            param_type="slider",
            name="Mutation Probability",
            value=1,
            min_value=0,
            max_value=100,
        )
        market_number = UserSettableParameter(
            param_type="slider",
            name="Market Number",
            value=0,
            min_value=0,
            max_value=size,
        )
        vaccination_center_number = UserSettableParameter(
            param_type="slider",
            name="Vaccination Center Number",
            value=0,
            min_value=0,
            max_value=size,
        )
        macron_starting_lockdown_minimal_ratio = UserSettableParameter(
            param_type="slider",
            name="Lockdown Start Ratio",
            value=10,
            min_value=0,
            max_value=100,
        )
        macron_stopping_lockdown_minimal_ratio = UserSettableParameter(
            param_type="slider",
            name="Lockdown End Ratio",
            value=5,
            min_value=0,
            max_value=100,
        )
        macron_lockdown_severity = UserSettableParameter(
            param_type="slider",
            name="Lockdown Severity",
            value=100,
            min_value=0,
            max_value=100,
        )
        macron_starting_lockdown_minimal_ratio_1 = UserSettableParameter(
            param_type="slider",
            name="Lockdown Start Ratio (Left side)",
            value=10,
            min_value=0,
            max_value=100,
        )
        macron_stopping_lockdown_minimal_ratio_1 = UserSettableParameter(
            param_type="slider",
            name="Lockdown End Ratio (Left side)",
            value=5,
            min_value=0,
            max_value=100,
        )
        macron_lockdown_severity_1 = UserSettableParameter(
            param_type="slider",
            name="Lockdown Severity (Left side)",
            value=100,
            min_value=0,
            max_value=100,
        )
        macron_starting_lockdown_minimal_ratio_2 = UserSettableParameter(
            param_type="slider",
            name="Lockdown Start Ratio (Right side)",
            value=10,
            min_value=0,
            max_value=100,
        )
        macron_stopping_lockdown_minimal_ratio_2 = UserSettableParameter(
            param_type="slider",
            name="Lockdown End Ratio (Right side)",
            value=5,
            min_value=0,
            max_value=100,
        )
        macron_lockdown_severity_2 = UserSettableParameter(
            param_type="slider",
            name="Lockdown Severity (Right side)",
            value=100,
            min_value=0,
            max_value=100,
        )
        hospital_bed = UserSettableParameter(
            param_type="slider",
            name="Hospital bed",
            value=50,
            min_value=0,
            max_value=100,
        )
        businessman_flight_probability = UserSettableParameter(
            param_type="slider",
            name="Flight Probability",
            value=5,
            min_value=0,
            max_value=100,
        )

        sliders = {
            "human_number": human_number,
            "infection_probability": infection_probability,
            "infection_duration": infection_duration,
            "death_probability": death_probability,
            "gilet_josne_number": gilet_josne_number,
            "businessman_number": businessman_number,
            "mutation_probability": mutation_probability,
            "market_number": market_number,
            "vaccination_center_number": vaccination_center_number,
            "macron_starting_lockdown_minimal_ratio": macron_starting_lockdown_minimal_ratio,
            "macron_stopping_lockdown_minimal_ratio": macron_stopping_lockdown_minimal_ratio,
            "macron_lockdown_severity": macron_lockdown_severity,
            "macron_starting_lockdown_minimal_ratio_1": macron_starting_lockdown_minimal_ratio_1,
            "macron_stopping_lockdown_minimal_ratio_1": macron_stopping_lockdown_minimal_ratio_1,
            "macron_lockdown_severity_1": macron_lockdown_severity_1,
            "macron_starting_lockdown_minimal_ratio_2": macron_starting_lockdown_minimal_ratio_2,
            "macron_stopping_lockdown_minimal_ratio_2": macron_stopping_lockdown_minimal_ratio_2,
            "macron_lockdown_severity_2": macron_lockdown_severity_2,
            "hospital_bed": hospital_bed,
            "businessman_flight_probability": businessman_flight_probability,
        }
        return sliders
