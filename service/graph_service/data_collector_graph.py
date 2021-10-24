import matplotlib.pyplot as plt
import seaborn as sns


class DataCollectorGraphService:
    @classmethod
    def generate_graph_combinations(cls, parameters):
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
            {
                "filename": cls.generate_filename("infected"),
                "values": [
                    'Infected',
                ]
            },
        ]
        if "hospital" in parameters and parameters["hospital"]:
            combinations.append(
                {
                    "filename": cls.generate_filename("hospital_dead"),
                    "values": [
                        'Hospital Occupancy',
                        'Dead'
                    ]
                }
            )
        if "countries_number" in parameters and parameters["countries_number"] == 1:
            combinations.append(
                {
                    "filename": cls.generate_filename("density"),
                    "values": [
                        'Density',
                    ]
                }
            )
        if "countries_number" in parameters and parameters["countries_number"] == 2:
            combinations.append(
                {
                    "filename": cls.generate_filename("density"),
                    "values": [
                        'Density (Left)',
                        'Density (Right)',
                    ]
                }
            )

        return combinations

    @staticmethod
    def generate_filename(filename):
        raise NotImplementedError

    @classmethod
    def plot(cls, parameters, title, source=None):
        combinations = cls.generate_graph_combinations(parameters=parameters)
        for combination in combinations:
            raw_df = cls.get_raw_variant_data(source)
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
    def get_raw_variant_data(source):
        raise NotImplementedError

    @staticmethod
    def clean_data(raw_df, values):
        raise NotImplementedError

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
            "Density": "tab:blue",
            "Density (Left)": "#224A979C",
            "Density (Right)": "#1143A0",
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
