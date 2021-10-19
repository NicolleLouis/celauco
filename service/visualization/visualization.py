from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.modules import ChartModule

from model.model.visualization_model import VisualizationModel
from service.geographic_service import GeographicService
from service.visualization.options import OptionService
from service.visualization.sliders import SliderService


class VisualizationService:
    @classmethod
    def display_model(
            cls,
            size=100,
            display_sliders={},
            walls=False,
            countries_number=1,
    ):
        grid = CanvasGrid(
            portrayal_method=cls.agent_portrayal,
            grid_width=size,
            grid_height=size,
            canvas_width=500,
            canvas_height=500,
        )
        model_params = cls.generate_model_params(
            size=size,
            display_sliders=display_sliders,
            walls=walls,
            countries_number=countries_number,
        )
        server = ModularServer(
            model_cls=VisualizationModel,
            visualization_elements=[grid, cls.get_charts(display_sliders)],
            model_params=model_params
        )
        server.port = 8521
        server.launch()

    @staticmethod
    def generate_model_params(
            size,
            walls,
            display_sliders,
            countries_number,
    ):
        sliders = SliderService.get_sliders(size=size)
        options = OptionService.get_options()

        model_params = {
            "human_number": sliders["human_number"],
            "width": size,
            "height": size,
            "maximum_number_of_turn": 10000,
            "countries_number": countries_number,
        }

        if "infection" in display_sliders and display_sliders["infection"]:
            model_params["infection_probability"] = sliders["infection_probability"]
            model_params["infection_duration"] = sliders["infection_duration"]
            model_params["death_probability"] = sliders["death_probability"]
            model_params["mutation_probability"] = sliders["mutation_probability"]

        if "macron" in display_sliders and display_sliders["macron"]:
            model_params["macron"] = options["macron"]
            model_params["macron_starting_lockdown_minimal_ratio"] = sliders['macron_starting_lockdown_minimal_ratio']
            model_params["macron_stopping_lockdown_minimal_ratio"] = sliders['macron_stopping_lockdown_minimal_ratio']
            model_params["macron_lockdown_severity"] = sliders['macron_lockdown_severity']
            model_params["macron_shut_down_market"] = options['macron_shut_down_market']

        if "hospital" in display_sliders and display_sliders["hospital"]:
            model_params["hospital"] = options["hospital"]
            model_params["hospital_bed"] = sliders["hospital_bed"]

        if walls:
            geographic_service = GeographicService(
                width=size,
                height=size,
            )
            wall_positions = geographic_service.vertical_line_positions()
            model_params["wall_positions"] = wall_positions

        if "market" in display_sliders and display_sliders["market"]:
            model_params["market_number"] = sliders["market_number"]

        if "other_humans" in display_sliders and display_sliders["other_humans"]:
            model_params["gilet_josne_number"] = sliders["gilet_josne_number"]
            model_params["businessman_number"] = sliders["businessman_number"]
            model_params["businessman_flight_probability"] = sliders["businessman_flight_probability"]
        return model_params

    @staticmethod
    def get_charts(display_sliders):
        chart_list = [
                {
                    "Label": "Infected",
                    "Color": "Red"
                },
                {
                    "Label": "Dead",
                    "Color": "Black"
                },
            ]
        if "hospital" in display_sliders and display_sliders["hospital"]:
            chart_list.append({
                    "Label": "Hospital Occupancy",
                    "Color": "Blue"
                })
        charts = ChartModule(
            chart_list,
            data_collector_name='graph_collector'
        )
        return charts

    @staticmethod
    def agent_portrayal(agent):
        return agent.display()