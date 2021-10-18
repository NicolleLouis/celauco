from model.batch import Batch
from service.graph_service.batch_run.infection_evolution import InfectionEvolutionBatchGraphService

parameters = {
    "human_number": 4000,
    "width": 100,
    "height": 100,
    "infection_probability": 10,
    "infection_duration": 30,
    "death_probability": 30,
    "mutation_probability": 0,
    "market_number": 35,
    "macron": True,
    "hospital": True,
    "log_variant_info": False,
    "businessman_number": 25,
}
title = 'Hospital'

batch = Batch(
    run_number=5,
    parameters=parameters
)
batch.run()
InfectionEvolutionBatchGraphService.plot(
    batch=batch,
    title=title,
)
