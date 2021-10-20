from service.graph_service.data_collector_graph import DataCollectorGraphService


class InfectionEvolutionSingleGraphService(DataCollectorGraphService):
    @staticmethod
    def generate_filename(filename):
        return "single/{}".format(filename)

    @staticmethod
    def get_raw_variant_data(model):
        return model.graph_collector.get_model_vars_dataframe()

    @staticmethod
    def clean_data(raw_df, values):
        cleaned_df = raw_df.rename_axis('Turn Number')
        cleaned_df = cleaned_df.reset_index()
        cleaned_df = cleaned_df.melt(id_vars=['Turn Number'], value_vars=values)
        return cleaned_df
