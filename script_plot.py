from model.model import CelaucoModel
from service.graph_service.single_run.infection_evolution import InfectionEvolutionSingleGraphService
from service.graph_service.single_run.variant_death import VariantDeathGraphService
from service.graph_service.single_run.variant_evolution import VariantEvolutionGraphService

model = CelaucoModel(
    human_number=1000,
    width=50,
    height=50,
    infection_probability=10,
    infection_duration=50,
    death_probability=1,
    mutation_probability=10,
    verbose=True,
)
model.run_model()

graph_services = [
    VariantEvolutionGraphService,
    VariantDeathGraphService,
    InfectionEvolutionSingleGraphService,
]
for service in graph_services:
    service.plot(model)
