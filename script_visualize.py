from service.visualization.visualization import VisualizationService

VisualizationService.display_model(
    size=100,
    walls=False,
    display_sliders={
        "infection": False,
        "macron": False,
        "hospital": True,
        "market": False,
        "other_humans": False,
    }
)
