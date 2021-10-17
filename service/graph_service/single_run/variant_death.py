import matplotlib.pyplot as plt


class VariantDeathGraphService:
    number_of_distinctive_variant = 5
    filename = "single/variant_death"

    @classmethod
    def plot(cls, model, title):
        raw_data = cls.get_raw_variant_data(model)
        data, labels = cls.clean_data(raw_data)
        cls.export_graph_in_file(
            data=data,
            labels=labels,
            title=title
        )

    @staticmethod
    def get_raw_variant_data(model):
        return model.known_infections

    @classmethod
    def clean_data(cls, raw_data):
        data = []
        labels = []
        ordered_variant = sorted(
            raw_data,
            key=lambda infection: infection.victim_number,
            reverse=True
        )
        distinctive_infection = ordered_variant[:cls.number_of_distinctive_variant]
        other_infection = ordered_variant[cls.number_of_distinctive_variant:]

        for infection in distinctive_infection:
            data.append(infection.victim_number)
            labels.append(infection.name)

        other_victim_number = sum(
            map(
                lambda infection: infection.victim_number,
                other_infection
            )
        )
        data.append(other_victim_number)
        labels.append("Other")

        return data, labels

    @classmethod
    def export_graph_in_file(
            cls,
            data,
            labels,
            title
    ):
        plt.figure()
        plt.title(title)
        plt.pie(data, labels=labels, autopct='%.0f%%')
        plt.savefig('graph/{}'.format(cls.filename))
