from model.batch import Batch
from service.graph_service.batch_run.infection_evolution import InfectionEvolutionBatchGraphService

parameters = {
    "human_number": 250,
    "width": 25,
    "height": 25,
    "infection_probability": 25,
    "infection_duration": 50,
    "death_probability": 1,
    "mutation_probability": 1,
    "market_number": 3,
    "macron": True,
}
batch = Batch(
    run_number=100,
    parameters=parameters
)
batch.run()
InfectionEvolutionBatchGraphService.plot(batch)
