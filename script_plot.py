from model.model.model import CelaucoModel
from service.geographic_service import GeographicService
from service.graph_service.single_run.infection_evolution import InfectionEvolutionSingleGraphService
from service.graph_service.single_run.variant_death import VariantDeathGraphService
from service.graph_service.single_run.variant_evolution import VariantEvolutionGraphService

wall_positions = GeographicService(
    width=100,
    height=100,
    model=None
).vertical_line_positions()

parameters = {
    "human_number": 2000,
    "width": 100,
    "height": 100,
    "infection_probability": 10,
    "infection_duration": 30,
    "death_probability": 30,
    "mutation_probability": 0,
    "verbose": True,
    "macron": False,
    "macron_parameters": {
        "starting_lockdown_minimal_ratio": 0.1,
    },
    'market_number': 35,
    'businessman_number': 0,
    'hospital': False,
    "countries_number": 2,
    "wall_positions": wall_positions
}

model = CelaucoModel(
    **parameters
)
title = "Test"

model.run_model()

graph_services = [
    VariantEvolutionGraphService,
    VariantDeathGraphService,
    InfectionEvolutionSingleGraphService
]
for service in graph_services:
    service.plot(
        source=model,
        title=title,
        parameters=parameters,
    )
