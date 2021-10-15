class GeographicService:
    def __init__(self, width, height):
        self.width = width
        self.height = height

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
