from mesa.visualization.UserParam import UserSettableParameter


class OptionService:
    @staticmethod
    def get_options():
        macron = UserSettableParameter(
            param_type="checkbox",
            name="Macron",
            value=False,
        )
        hospital = UserSettableParameter(
            param_type="checkbox",
            name="Hospital",
            value=False,
        )
        options = {
            "macron": macron,
            "hospital": hospital,
        }
        return options
