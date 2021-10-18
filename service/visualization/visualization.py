from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.modules import ChartModule

from model.model.visualization_model import VisualizationModel
from service.geographic_service import GeographicService
from service.visualization.options import OptionService
from service.visualization.sliders import SliderService


class VisualizationService:
    @classmethod
    def display_model(cls, size=100):
        grid = CanvasGrid(
            portrayal_method=cls.agent_portrayal,
            grid_width=size,
            grid_height=size,
            canvas_width=500,
            canvas_height=500,
        )
        geographic_service = GeographicService(
            width=size,
            height=size,
        )
        sliders = SliderService.get_sliders(size=size)
        options = OptionService.get_options()
        wall_positions = geographic_service.vertical_line_positions()
        server = ModularServer(
            model_cls=VisualizationModel,
            visualization_elements=[grid, cls.get_charts()],
            model_params={
                "human_number": sliders["human_number"],
                "infection_probability": sliders["infection_probability"],
                "infection_duration": sliders["infection_duration"],
                "death_probability": sliders["death_probability"],
                "gilet_josne_number": sliders["gilet_josne_number"],
                "businessman_number": sliders["businessman_number"],
                "mutation_probability": sliders["mutation_probability"],
                "market_number": sliders["market_number"],
                "width": size,
                "height": size,
                "macron": options["macron"],
                "macron_starting_lockdown_minimal_ratio": sliders['macron_starting_lockdown_minimal_ratio'],
                "hospital": options["hospital"],
                "maximum_number_of_turn": 10000,
                # "wall_positions": wall_positions,
            }
        )
        server.port = 8521
        server.launch()


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
                {
                    "Label": "Hospital Occupancy",
                    "Color": "Blue"
                },
            ],
            data_collector_name='graph_collector'
        )
        return charts

    @staticmethod
    def agent_portrayal(agent):
        return agent.display()
