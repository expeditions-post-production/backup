class Name:
    def __init__(self, name):
        self.rus = name[0]
        self.eng = name[1]
        self.local = name[2]

    def __repr__(self):
        return f"Name(rus={self.rus}, eng={self.eng}, local={self.local})"


class Coordinates:
    def __init__(self, coordinates):
        split_coords = coordinates[0].split(", ")
        self.lat = split_coords[0]
        self.long = split_coords[1]

    def __repr__(self):
        return f"Coordinates(lat={self.lat}, long={self.long})"
