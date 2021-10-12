from model.model import CelaucoModel
from service.graph_service.infection_evolution import InfectionEvolutionGraphService
from service.graph_service.variant_death import VariantDeathGraphService
from service.graph_service.variant_evolution import VariantEvolutionGraphService

model = CelaucoModel(
    human_number=200,
    width=25,
    height=25,
    infection_probability=10,
    infection_duration=50,
    death_probability=1,
    mutation_probability=10,
)
model.run_model()

graph_services = [
    VariantEvolutionGraphService,
    VariantDeathGraphService,
    InfectionEvolutionGraphService,
]
for service in graph_services:
    service.plot(model)
