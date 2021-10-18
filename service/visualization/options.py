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
        macron_shut_down_market = UserSettableParameter(
            param_type="checkbox",
            name="Macron Shut Down Market",
            value=False,
        )
        options = {
            "macron": macron,
            "macron_shut_down_market": macron_shut_down_market,
            "hospital": hospital,
        }
        return options
