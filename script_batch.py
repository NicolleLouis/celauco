from model.batch import Batch
from service.graph_service.batch_run.infection_evolution import InfectionEvolutionBatchGraphService

parameters = {
    "human_number": 3000,
    "width": 100,
    "height": 100,
    "infection_probability": 10,
    "infection_duration": 30,
    "death_probability": 1,
    "mutation_probability": 0,
    "market_number": 50,
    "macron": True,
    "log_variant_info": False,
}
batch = Batch(
    run_number=100,
    parameters=parameters
)
batch.run()
InfectionEvolutionBatchGraphService.plot(batch)
