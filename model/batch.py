from model.model.model import CelaucoModel
import pandas as pd


class Batch:
    def __init__(
            self,
            run_number: int,
            parameters: dict = {},
    ):
        self.parameters = parameters
        self.run_number = run_number
        self.data_collector = pd.DataFrame(
            columns=["Healthy", "Infected", "Dead"]
        )

    def run(self):
        for run_number in range(self.run_number):
            print("Run number: {}".format(run_number))
            model = CelaucoModel(**self.parameters)
            model.run_model()
            df = model.graph_collector.get_model_vars_dataframe()
            self.data_collector = self.data_collector.append(df)
