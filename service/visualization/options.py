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
        macron_shut_down_market_1 = UserSettableParameter(
            param_type="checkbox",
            name="Macron Shut Down Market (Left side)",
            value=False,
        )
        macron_shut_down_market_2 = UserSettableParameter(
            param_type="checkbox",
            name="Macron Shut Down Market (Right side)",
            value=False,
        )
        options = {
            "macron": macron,
            "macron_shut_down_market": macron_shut_down_market,
            "macron_shut_down_market_1": macron_shut_down_market_1,
            "macron_shut_down_market_2": macron_shut_down_market_2,
            "hospital": hospital,
        }
        return options
