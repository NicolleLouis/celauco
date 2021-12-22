from service.visualization.visualization import VisualizationService

VisualizationService.display_model(
    size=100,
    walls=False,
    display_sliders={
        "infection": True,
        "macron": True,
        "hospital": False,
        "market": True,
        "other_humans": False,
        "vaccination_center": False,
    },
    countries_number=1,
)
