from model.country import Country


class GeographicService:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def generate_countries(self, countries_number=1):
        if countries_number == 1:
            country = Country(
                position_bottom_left=(0, 0),
                position_top_right=(self.width, self.height)
            )
            return [country]
        if countries_number == 2:
            middle_width = int(self.width/2)
            country_1 = Country(
                position_bottom_left=(0, 0),
                position_top_right=(middle_width, self.height)
            )
            country_2 = Country(
                position_bottom_left=(middle_width + 1, 0),
                position_top_right=(self.width, self.height)
            )
            return [country_1, country_2]

    def vertical_line_positions(self):
        positions = []
        middle_position = int(self.width/2)
        for y in range(self.height):
            positions.append((middle_position, y))
        return positions

    def vertical_line_middle_hole_positions(self):
        positions = []
        middle_position = int(self.width / 2)
        for y in range(self.height):
            if y != int(self.height/2):
                positions.append((middle_position, y))
        return positions
