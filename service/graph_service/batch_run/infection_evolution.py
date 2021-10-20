import matplotlib.pyplot as plt
import seaborn as sns

from service.graph_service.data_collector_graph import DataCollectorGraphService


class InfectionEvolutionBatchGraphService(DataCollectorGraphService):
    @staticmethod
    def get_raw_variant_data(batch):
        return batch.data_collector

    @staticmethod
    def generate_filename(filename):
        return "batch/{}".format(filename)

    @staticmethod
    def clean_data(raw_df, values):
        cleaned_df = raw_df.rename_axis('Turn Number')
        cleaned_df = cleaned_df.reset_index()
        cleaned_df = cleaned_df.melt(id_vars=['Turn Number'], value_vars=values)
        return cleaned_df

