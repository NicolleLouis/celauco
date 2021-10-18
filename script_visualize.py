from service.visualization.visualization import VisualizationService

VisualizationService.display_model(
    size=100,
    walls=False,
    display_sliders={
        "infection": False,
        "macron": True,
        "hospital": False,
        "market": True,
        "other_humans": False,
    }
)
