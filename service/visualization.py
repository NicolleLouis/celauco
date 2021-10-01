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
                {
                    "Label": "Healthy",
                    "Color": "Green"
                },
                {
                    "Label": "Infected",
                    "Color": "Red"
                },
                # {
                #     "Label": "Immune",
                #     "Color": "Blue"
                # },
                {
                    "Label": "Dead",
                    "Color": "Black"
                },
            ],
            data_collector_name='data_collector'
        )
        return charts

    @staticmethod
    def agent_portrayal(agent):
        return agent.display()

    @staticmethod
    def get_sliders(size):
        human_number = UserSettableParameter(
            param_type="slider",
            name="Human number",
            value=size*4,
            min_value=0,
            max_value=size*10,
        )
        businessman_number = UserSettableParameter(
            param_type="slider",
            name="BusinessMan number",
            value=0,
            min_value=0,
            max_value=size * 10,
        )
        medic_number = UserSettableParameter(
            param_type="slider",
            name="Medic number",
            value=0,
            min_value=0,
            max_value=int(size/5),
        )
        gilet_josne_number = UserSettableParameter(
            param_type="slider",
            name="Gilet Josne number",
            value=0,
            min_value=0,
            max_value=size,
        )
        initially_infected = UserSettableParameter(
            param_type="slider",
            name="Agent initially infected",
            value=1,
            min_value=1,
            max_value=50,
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
            name="Death probabity",
            value=1,
            min_value=0,
            max_value=100,
        )
        sliders = {
            "human_number": human_number,
            # "initially_infected": initially_infected,
            "infection_probability": infection_probability,
            "infection_duration": infection_duration,
            "death_probability": death_probability,
            "medic_number": medic_number,
            "gilet_josne_number": gilet_josne_number,
            "businessman_number": businessman_number,
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
                # "initially_infected": sliders["initially_infected"],
                "width": size,
                "height": size,
            }
        )
        server.port = 8521
        server.launch()
