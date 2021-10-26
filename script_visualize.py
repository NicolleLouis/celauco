from service.visualization.visualization import VisualizationService

VisualizationService.display_model(
    size=100,
    walls=False,
    display_sliders={
        "infection": True,
        "macron": False,
        "hospital": False,
        "market": False,
        "other_humans": False,
        "vaccination_center": True,
    },
    countries_number=1,
)
