class Country:
    def __init__(
            self,
            position_bottom_left,
            position_top_right,
    ):
        x_1, y_1 = position_bottom_left
        x_2, y_2 = position_top_right
        self.positions = []

        for x in range(x_1, x_2):
            for y in range(y_1, y_2):
                self.positions.append((x, y))
