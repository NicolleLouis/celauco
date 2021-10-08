from model.model import CelaucoModel
from service.infection_service import InfectionService
from service.visualization import Visualization

model = CelaucoModel(human_number=10)
model.run_model()
print(model.variant_collector.get_model_vars_dataframe().to_dict()["Variant"])
