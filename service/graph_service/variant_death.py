import matplotlib.pyplot as plt


class VariantDeathGraphService:
    number_of_distinctive_variant = 5

    @classmethod
    def plot(cls, model):
        raw_data = cls.get_raw_variant_data(model)
        data, labels = cls.clean_data(raw_data)
        cls.export_graph_in_file(data=data, labels=labels)

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

    @staticmethod
    def export_graph_in_file(
            data,
            labels,
            filename="variant_death"
    ):
        plt.figure()
        plt.pie(data, labels=labels, autopct='%.0f%%')
        plt.savefig('graph/{}'.format(filename))
