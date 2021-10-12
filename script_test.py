from model.batch import Batch
from service.graph_service.batch_run.infection_evolution import InfectionEvolutionBatchGraphService

batch = Batch(run_number=100)
batch.run()
InfectionEvolutionBatchGraphService.plot(batch)
