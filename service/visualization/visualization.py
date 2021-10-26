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
        charts = cls.get_charts(
                display_sliders=display_sliders,
                countries_number=countries_number,
            )
        density_charts = cls.get_density_charts(
            display_sliders=display_sliders,
            countries_number=countries_number,
        )
        server = ModularServer(
            model_cls=VisualizationModel,
            visualization_elements=[
                grid,
                charts,
                density_charts
            ],
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
            if countries_number == 1:
                model_params["macron_starting_lockdown_minimal_ratio"] = sliders[
                    'macron_starting_lockdown_minimal_ratio'
                ]
                model_params["macron_stopping_lockdown_minimal_ratio"] = sliders[
                    'macron_stopping_lockdown_minimal_ratio'
                ]
                model_params["macron_lockdown_severity"] = sliders['macron_lockdown_severity']
            if countries_number == 2:
                model_params["macron_starting_lockdown_minimal_ratio_1"] = sliders[
                    'macron_starting_lockdown_minimal_ratio_1'
                ]
                model_params["macron_stopping_lockdown_minimal_ratio_1"] = sliders[
                    'macron_stopping_lockdown_minimal_ratio_1'
                ]
                model_params["macron_lockdown_severity_1"] = sliders['macron_lockdown_severity_1']
                model_params["macron_starting_lockdown_minimal_ratio_2"] = sliders[
                    'macron_starting_lockdown_minimal_ratio_2'
                ]
                model_params["macron_stopping_lockdown_minimal_ratio_2"] = sliders[
                    'macron_stopping_lockdown_minimal_ratio_2'
                ]
                model_params["macron_lockdown_severity_2"] = sliders['macron_lockdown_severity_2']
            if "market" in display_sliders and display_sliders["market"]:
                if countries_number == 1:
                    model_params["macron_shut_down_market"] = options['macron_shut_down_market']
                if countries_number == 2:
                    model_params["macron_shut_down_market_1"] = options['macron_shut_down_market_1']
                    model_params["macron_shut_down_market_2"] = options['macron_shut_down_market_2']

        if "hospital" in display_sliders and display_sliders["hospital"]:
            model_params["hospital"] = options["hospital"]
            model_params["hospital_bed"] = sliders["hospital_bed"]

        if walls:
            geographic_service = GeographicService(
                width=size,
                height=size,
                model=None,
            )
            wall_positions = geographic_service.vertical_line_positions()
            model_params["wall_positions"] = wall_positions

        if "market" in display_sliders and display_sliders["market"]:
            model_params["market_number"] = sliders["market_number"]

        if "vaccination_center" in display_sliders and display_sliders["vaccination_center"]:
            model_params["vaccination_center_number"] = sliders["vaccination_center_number"]

        if "other_humans" in display_sliders and display_sliders["other_humans"]:
            model_params["gilet_josne_number"] = sliders["gilet_josne_number"]
            model_params["businessman_number"] = sliders["businessman_number"]
            model_params["businessman_flight_probability"] = sliders["businessman_flight_probability"]
        return model_params

    @staticmethod
    def get_charts(display_sliders, countries_number):
        chart_list = [
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

        if countries_number == 1:
            chart_list.append({
                "Label": "Infected",
                "Color": "Red"
            })

        if countries_number == 2:
            chart_list.append({
                "Label": "Infected (Left)",
                "Color": "#58A0EB"
            })
            chart_list.append({
                "Label": "Infected (Right)",
                "Color": "#112BDF"
            })

        charts = ChartModule(
            chart_list,
            data_collector_name='graph_collector'
        )
        return charts

    @staticmethod
    def get_density_charts(display_sliders, countries_number):
        chart_list = []
        if countries_number == 1:
            chart_list.append({
                "Label": "Density",
                "Color": "Green"
            })

        if countries_number == 2:
            chart_list.append({
                "Label": "Density (Left)",
                "Color": "#12791370"
            })
            chart_list.append({
                "Label": "Density (Right)",
                "Color": "#095D0A"
            })

        charts = ChartModule(
            chart_list,
            data_collector_name='graph_collector'
        )
        return charts

    @staticmethod
    def agent_portrayal(agent):
        return agent.display()
