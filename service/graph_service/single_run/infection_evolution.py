import matplotlib.pyplot as plt
import seaborn as sns

from model.non_human_agents.hospital import Hospital


class InfectionEvolutionSingleGraphService:
    @classmethod
    def generate_graph_combinations(cls, model):
        combinations = [
            {
                "filename": cls.generate_filename("healthy_infected_dead"),
                "values": [
                    'Healthy',
                    'Infected',
                    'Dead'
                ]
            },
            {
                "filename": cls.generate_filename("infected_dead"),
                "values": [
                    'Infected',
                    'Dead'
                ]
            },
        ]
        if len(model.get_all_agent_of_class(Hospital)) > 0:
            combinations.append(
                {
                    "filename": cls.generate_filename("hospital_dead"),
                    "values": [
                        'Hospital Occupancy',
                        'Dead'
                    ]
                }
            )

        return combinations

    @staticmethod
    def generate_filename(filename):
        return "single/{}".format(filename)

    @classmethod
    def plot(cls, model, title):
        combinations = cls.generate_graph_combinations(model=model)
        for combination in combinations:
            raw_df = cls.get_raw_variant_data(model)
            cleaned_df = cls.clean_data(
                raw_df=raw_df,
                values=combination["values"],
            )
            cls.export_graph_in_file(
                data=cleaned_df,
                title=title,
                filename=combination["filename"],
            )

    @staticmethod
    def get_raw_variant_data(model):
        return model.graph_collector.get_model_vars_dataframe()

    @staticmethod
    def clean_data(raw_df, values):
        cleaned_df = raw_df.rename_axis('Turn Number')
        cleaned_df = cleaned_df.reset_index()
        cleaned_df = cleaned_df.melt(id_vars=['Turn Number'], value_vars=values)
        return cleaned_df

    @classmethod
    def export_graph_in_file(
            cls,
            data,
            title,
            filename,
    ):
        plt.figure()
        palette = {
            "Healthy": "tab:green",
            "Infected": "tab:red",
            "Dead": "tab:grey",
            "Hospital Occupancy": "tab:blue",
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
            title=title
        )
        plt.savefig('graph/{}'.format(filename))
