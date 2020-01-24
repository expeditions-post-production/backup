from api.db_handler import db_utils


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


class ExpSeries:
    def __init__(self, series_idx):
        self.idx = series_idx
        self.name = self.get_series_name()

    def get_series_name(self):
        db = db_utils.Database()
        name = db.execute("SELECT series_name FROM basic_info WHERE series_id = ?", (self.idx,))
        return name[0][0]


class DirectionContent:
    def __init__(self, dir_name):
        self.direction = dir_name
        self.series = self.get_series()

    def get_series(self):
        db = db_utils.Database()
        series = db.execute("SELECT series_id FROM basic_info WHERE direction = ?", (self.direction,))
        return [ExpSeries(s[0]) for s in series]


class Photo:
    def __init__(self, info, idx):
        self.route = "../static/photos/" + info.split(":")[0]
        self.description = info.split(":")[1]
        self.if_active = ""
        self.idx = idx


class Village:
    def __init__(self, idx):
        self.idx = idx
        self.name = self.get_name()

    def get_name(self):
        db = db_utils.Database()
        name = db.execute("SELECT name_rus FROM villages WHERE village_id = ?", (self.idx,))
        return name[0][0]