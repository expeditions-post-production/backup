from FieldTrips.db_handler import db_utils
from FieldTrips.utils.support_structures import Village


class ExpSearchUnit:
    def __init__(self, data):
        self.series_id = data[0]
        self.series_name = data[1]
        self.years = data[2]
        self.direction = data[3]
        self.village = Village(data[4])
        self.supervisor = self.get_supervisor()

    def get_supervisor(self):
        supervisors = []
        db = db_utils.Database()
        exps = db.execute("SELECT expedition_id FROM expeditions WHERE series_id = ?", (self.series_id,))
        for exp in exps:
            supervisor = db.execute("SELECT name FROM participants WHERE expedition_id = ? AND supervisor = ?",
                                    (exp[0], "да"))
            for sup in supervisor:
                if sup[0] not in supervisors:
                    supervisors.append(sup[0])
        return ", ".join(supervisors)


class SearchInfo:
    def __init__(self):
        self.expeditions = self.get_expeditions()

    @staticmethod
    def get_expeditions():
        db = db_utils.Database()
        series = db.execute("SELECT series_id, series_name, years, direction, main_village FROM basic_info")
        return [ExpSearchUnit(data) for data in series]
