from model.batch import Batch
from service.graph_service.batch_run.infection_evolution import InfectionEvolutionBatchGraphService

parameters = {
    "human_number": 10,
    "width": 100,
    "height": 100,
    "infection_probability": 10,
    "infection_duration": 30,
    "death_probability": 5,
    "mutation_probability": 0,
    "market_number": 50,
    "macron": True,
    "hospital": True,
    "log_variant_info": False,
    "businessman_number": 200,
}
title = 'Titre'

batch = Batch(
    run_number=100,
    parameters=parameters
)
batch.run()
InfectionEvolutionBatchGraphService.plot(
    batch=batch,
    title=title,
)
