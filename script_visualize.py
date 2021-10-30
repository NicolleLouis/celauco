from service.visualization.visualization import VisualizationService

VisualizationService.display_model(
    size=25,
    walls=True,
    display_sliders={
        "infection": True,
        "macron": True,
        "hospital": False,
        "market": True,
        "other_humans": True,
        "vaccination_center": False,
    },
    countries_number=2,
)
