from service.visualization.visualization import VisualizationService

VisualizationService.display_model(
    size=100,
    walls=True,
    display_sliders={
        "infection": False,
        "macron": True,
        "hospital": False,
        "market": False,
        "other_humans": False,
    },
    countries_number=2,
)
