from model.model.model import CelaucoModel
from service.graph_service.single_run.infection_evolution import InfectionEvolutionSingleGraphService
from service.graph_service.single_run.variant_death import VariantDeathGraphService
from service.graph_service.single_run.variant_evolution import VariantEvolutionGraphService

model = CelaucoModel(
    human_number=4000,
    width=100,
    height=100,
    infection_probability=10,
    infection_duration=30,
    death_probability=1,
    mutation_probability=1,
    verbose=True,
    macron=True,
    market_number=35,
    businessman_number=0,
    hospital=True,
)
title = "Test"

model.run_model()

graph_services = [
    VariantEvolutionGraphService,
    VariantDeathGraphService,
    InfectionEvolutionSingleGraphService,
]
for service in graph_services:
    service.plot(
        model=model,
        title=title
    )
