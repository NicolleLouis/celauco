from model.model import CelaucoModel

model = CelaucoModel(
    human_number=100,
    width=25,
    height=25,
    infection_probability=25,
    infection_duration=50,
    death_probability=5,
    mutation_probability=5,
)
model.run_model()
print(model.graph_collector.get_model_vars_dataframe())
print(model.variant_collector.get_model_vars_dataframe().to_dict()["variant_data"])
