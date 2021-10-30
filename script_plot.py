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
    "human_number": 2950,
    "width": 100,
    "height": 100,
    "infection_probability": 10,
    "infection_duration": 50,
    "death_probability": 3,
    "mutation_probability": 0,
    "verbose": True,
    "macron": True,
    "macron_parameters": [
        {
            "lockdown_severity": 100,
            "starting_lockdown_minimal_ratio": 10,
            "stopping_lockdown_minimal_ratio": 1,
        },
        {
            "lockdown_severity": 100,
            "starting_lockdown_minimal_ratio": 20,
            "stopping_lockdown_minimal_ratio": 1,
        },
    ],
    'market_number': 20,
    'businessman_number': 50,
    'hospital': True,
    "hospital_parameters": {
        'hospital_bed': 30,
    },
    "countries_number": 2,
    "wall_positions": wall_positions
}
title = "Country co-evolution"

model = CelaucoModel(
    **parameters
)

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
