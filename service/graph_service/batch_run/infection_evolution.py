import matplotlib.pyplot as plt
import seaborn as sns


class InfectionEvolutionBatchGraphService:
    filename = "batch/infection_evolution"

    @classmethod
    def plot(cls, batch, title):
        raw_df = cls.get_raw_variant_data(batch)
        cleaned_df = cls.clean_data(raw_df)
        cls.export_graph_in_file(data=cleaned_df, title=title)

    @staticmethod
    def get_raw_variant_data(batch):
        return batch.data_collector

    @staticmethod
    def clean_data(raw_df):
        cleaned_df = raw_df.rename_axis('Turn Number')
        cleaned_df = cleaned_df.reset_index()
        cleaned_df = cleaned_df.melt(id_vars=['Turn Number'], value_vars=[
            'Healthy',
            'Infected',
            'Dead'
        ])
        return cleaned_df

    @classmethod
    def export_graph_in_file(
            cls,
            data,
            title
    ):
        plt.figure()
        palette = {
            "Healthy": "tab:green",
            "Infected": "tab:red",
            "Dead": "tab:grey"
        }
        ax = sns.lineplot(
            x="Turn Number",
            y="value",
            hue="variable",
            palette=palette,
            data=data,
        )
        ax.set(
            ylabel="Human Number",
            title=title,
        )
        plt.savefig('graph/{}'.format(cls.filename))
