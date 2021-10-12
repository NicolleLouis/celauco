import matplotlib.pyplot as plt
import seaborn as sns


class InfectionEvolutionGraphService:
    filename = "infection_evolution"

    @classmethod
    def plot(cls, model):
        raw_df = cls.get_raw_variant_data(model)
        cleaned_df = cls.clean_data(raw_df)
        cls.export_graph_in_file(data=cleaned_df)

    @staticmethod
    def get_raw_variant_data(model):
        return model.graph_collector.get_model_vars_dataframe()

    @staticmethod
    def clean_data(raw_df):
        cleaned_df = raw_df.rename_axis('Turn Number')
        cleaned_df = cleaned_df.reset_index()
        cleaned_df = cleaned_df.melt(id_vars=['Turn Number'], value_vars=['Healthy', 'Infected', 'Dead'])
        return cleaned_df

    @classmethod
    def export_graph_in_file(
            cls,
            data,
    ):
        plt.figure()
        palette = {
            "Healthy": "tab:green",
            "Infected": "tab:red",
            "Dead": "tab:grey"
        }
        sns.lineplot(
            x="Turn Number",
            y="value",
            hue="variable",
            palette=palette,
            data=data,
        )
        plt.savefig('graph/{}'.format(cls.filename))
