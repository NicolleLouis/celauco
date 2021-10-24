class Country:
    def __init__(
            self,
            model,
            position_bottom_left,
            position_top_right,
    ):
        self.model = model

        x_1, y_1 = position_bottom_left
        x_2, y_2 = position_top_right

        self.positions = []

        for x in range(x_1, x_2):
            for y in range(y_1, y_2):
                self.positions.append((x, y))

        self.size = len(self.positions)

    @property
    def density(self):
        agents = self.model.get_all_humans(country=self)
        return 100*len(agents)/self.size
