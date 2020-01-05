from api.db_handler import db_utils
from api.utils import support_structures as sup


class Village:
    def __init__(self, village_id):
        self.idx = village_id
        self.name = self.get_name()
        self.coords = self.get_coordinates()

    def get_name(self):
        db = db_utils.Database()
        name = db.execute("SELECT name_rus, name_latin, name_local FROM villages WHERE village_id = ?", (self.idx,))
        return sup.Name(name[0])

    def get_coordinates(self):
        db = db_utils.Database()
        coords = db.execute("SELECT coordinates FROM villages WHERE village_id = ?", (self.idx,))
        return sup.Coordinates(coords[0])