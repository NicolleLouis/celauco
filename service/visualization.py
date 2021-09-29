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
                {
                    "Label": "Immune",
                    "Color": "Blue"
                },
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
    def get_sliders():
        agents_number = UserSettableParameter(
            param_type="slider",
            name="Agent Numbers",
            value=20,
            min_value=1,
            max_value=50,
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
            value=25,
            min_value=0,
            max_value=100,
        )
        infection_duration = UserSettableParameter(
            param_type="slider",
            name="Infection duration",
            value=10,
            min_value=1,
            max_value=50,
        )
        death_probability = UserSettableParameter(
            param_type="slider",
            name="Death probabity",
            value=1,
            min_value=1,
            max_value=100,
        )
        return agents_number, initially_infected, infection_probability, infection_duration, death_probability

    @classmethod
    def display_model(cls):
        grid = CanvasGrid(cls.agent_portrayal, 10, 10, 500, 500)
        agents_number, initially_infected, infection_probability, infection_duration, death_probability = cls.get_sliders()
        server = ModularServer(
            model_cls=CelaucoModel,
            visualization_elements=[grid, cls.get_charts()],
            model_params={
                "agents_number": agents_number,
                "infection_probability": infection_probability,
                "infection_duration": infection_duration,
                "death_probability": death_probability,
                "initially_infected": initially_infected,
                "width": 10,
                "height": 10,
            }
        )
        server.port = 8521
        server.launch()
