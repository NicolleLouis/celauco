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
    "human_number": 3000,
    "width": 100,
    "height": 100,
    "infection_probability": 10,
    "infection_duration": 30,
    "death_probability": 30,
    "mutation_probability": 0,
    "verbose": True,
    "macron": True,
    "macron_parameters": [
        {
            "lockdown_severity": 100
        },
        {
            "lockdown_severity": 60
        },
    ],
    'market_number': 50,
    'businessman_number': 25,
    'hospital': False,
    "countries_number": 2,
    "wall_positions": wall_positions
}

model = CelaucoModel(
    **parameters
)

title = 'Left side lockdown/Right side curfew'

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
