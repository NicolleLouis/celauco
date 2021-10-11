from model.model import CelaucoModel
from service.graph.variant_evolution import ModelGraphService

model = CelaucoModel(
    human_number=200,
    width=25,
    height=25,
    infection_probability=10,
    infection_duration=50,
    death_probability=1,
    mutation_probability=10,
)
data = ModelGraphService.get_variant_data(model)
