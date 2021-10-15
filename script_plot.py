from model.model import CelaucoModel
from service.graph_service.single_run.infection_evolution import InfectionEvolutionSingleGraphService
from service.graph_service.single_run.variant_death import VariantDeathGraphService
from service.graph_service.single_run.variant_evolution import VariantEvolutionGraphService

model = CelaucoModel(
    human_number=3000,
    width=100,
    height=100,
    infection_probability=10,
    infection_duration=30,
    death_probability=1,
    mutation_probability=0,
    verbose=True,
    macron=True,
    market_number=50,
    businessman_number=25,
    wall_positions=[1, 2, 3],
)
model.run_model()

graph_services = [
    VariantEvolutionGraphService,
    VariantDeathGraphService,
    InfectionEvolutionSingleGraphService,
]
for service in graph_services:
    service.plot(model)
