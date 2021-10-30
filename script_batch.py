from model.batch import Batch
from service.geographic_service import GeographicService
from service.graph_service.batch_run.infection_evolution import InfectionEvolutionBatchGraphService

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
