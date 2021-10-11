import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


class ModelGraphService:
    @staticmethod
    def get_raw_variant_data(model):
        return model.variant_collector.get_model_vars_dataframe().to_dict()["variant_data"]

    @classmethod
    def convert_variant_data(cls, raw_data, biggest_infections_name):
        data = []
        for turn_number, variant_info in raw_data.items():
            for variant_name, number_of_infected in variant_info.items():
                if variant_name in biggest_infections_name:
                    data.append([variant_name, turn_number, number_of_infected])
        df = pd.DataFrame(data, columns=['Variant', 'Turn Number', 'Number of infected'])
        return df

    @classmethod
    def get_variant_data(cls, model):
        model.run_model()
        raw_data = cls.get_raw_variant_data(model)
        biggest_infections_name = model.get_biggest_infections_name()
        cleaned_data = cls.convert_variant_data(raw_data, biggest_infections_name)
        cls.export_graph_in_file(data=cleaned_data)

    @classmethod
    def export_graph_in_file(cls, data, filename="covid_variant.png"):
        sns.lineplot(
            y='Number of infected',
            x='Turn Number',
            hue="Variant",
            data=data,
        )
        plt.savefig('graph/{}'.format(filename))

    @staticmethod
    def get_length_of_infection(raw_data):
        return len(raw_data)
