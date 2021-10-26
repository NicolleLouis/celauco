from model.batch import Batch
from service.geographic_service import GeographicService
from service.graph_service.batch_run.infection_evolution import InfectionEvolutionBatchGraphService

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
    "death_probability": 3,
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
title = 'Left side lockdown/Right side curfew'

batch = Batch(
    run_number=25,
    parameters=parameters
)
batch.run()
InfectionEvolutionBatchGraphService.plot(
    source=batch,
    title=title,
    parameters=parameters,
)
