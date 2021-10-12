from model.batch import Batch
from service.graph_service.batch_run.infection_evolution import InfectionEvolutionBatchGraphService

parameters = {
    "human_number": 250,
    "medic_number": 5,
    "gilet_josne_number": 0,
    "businessman_number": 0,
    "width": 25,
    "height": 25,
    "infection_probability": 25,
    "infection_duration": 50,
    "death_probability": 5,
    "mutation_probability": 0,
}
batch = Batch(
    run_number=100,
    parameters=parameters
)
batch.run()
InfectionEvolutionBatchGraphService.plot(batch)
