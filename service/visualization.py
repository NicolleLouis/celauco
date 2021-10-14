from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import UserSettableParameter
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.modules import ChartModule
from model.model import CelaucoModel


class Visualization:
    @staticmethod
    def get_charts():
        charts = ChartModule(
            [
                # {
                #     "Label": "Healthy",
                #     "Color": "Green"
                # },
                {
                    "Label": "Infected",
                    "Color": "Red"
                },
                {
                    "Label": "Dead",
                    "Color": "Black"
                },
            ],
            data_collector_name='graph_collector'
        )
        return charts

    @staticmethod
    def agent_portrayal(agent):
        return agent.display()

    @staticmethod
    def get_options():
        macron = UserSettableParameter(
            param_type="checkbox",
            name="Macron",
            value=False,
        )
        options = {
            "macron": macron
        }
        return options

    @staticmethod
    def get_sliders(size):
        human_number = UserSettableParameter(
            param_type="slider",
            name="Human number",
            value=int(size*size/5),
            min_value=0,
            max_value=size*size,
        )
        businessman_number = UserSettableParameter(
            param_type="slider",
            name="BusinessMan number",
            value=0,
            min_value=0,
            max_value=size*size,
        )
        medic_number = UserSettableParameter(
            param_type="slider",
            name="Medic number",
            value=0,
            min_value=0,
            max_value=size,
        )
        gilet_josne_number = UserSettableParameter(
            param_type="slider",
            name="Party Monsters number",
            value=0,
            min_value=0,
            max_value=size*size,
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
        sliders = {
            "human_number": human_number,
            "infection_probability": infection_probability,
            "infection_duration": infection_duration,
            "death_probability": death_probability,
            "medic_number": medic_number,
            "gilet_josne_number": gilet_josne_number,
            "businessman_number": businessman_number,
            "mutation_probability": mutation_probability,
            "market_number": market_number,
        }
        return sliders

    @classmethod
    def display_model(cls, size=10):
        grid = CanvasGrid(
            portrayal_method=cls.agent_portrayal,
            grid_width=size,
            grid_height=size,
            canvas_width=500,
            canvas_height=500,
        )
        sliders = cls.get_sliders(size=size)
        options = cls.get_options()
        server = ModularServer(
            model_cls=CelaucoModel,
            visualization_elements=[grid, cls.get_charts()],
            model_params={
                "human_number": sliders["human_number"],
                "infection_probability": sliders["infection_probability"],
                "infection_duration": sliders["infection_duration"],
                "death_probability": sliders["death_probability"],
                "medic_number": sliders["medic_number"],
                "gilet_josne_number": sliders["gilet_josne_number"],
                "businessman_number": sliders["businessman_number"],
                "mutation_probability": sliders["mutation_probability"],
                "market_number": sliders["market_number"],
                "width": size,
                "height": size,
                "macron": options["macron"],
                "maximum_number_of_turn": 10000,
            }
        )
        server.port = 8521
        server.launch()
