from FieldTrips.db_handler import db_utils
from FieldTrips.utils import support_structures as sup


class Expedition:
    def __init__(self, expedition_idx, number):
        self.idx = expedition_idx
        self.publications = "<br><br>".join(self.get_publications())
        self.participants = self.get_participants()
        self.year = self.get_year()
        self.villages = self.get_villages()
        self.if_active = " show active" if number == 0 else ""

    def get_year(self):
        db = db_utils.Database()
        year = db.execute("SELECT year FROM expeditions WHERE expedition_id = ?", (self.idx,))
        return year[0][0] if year else None

    def get_publications(self):
        db = db_utils.Database()
        publ = db.execute("SELECT publications FROM expeditions WHERE expedition_id = ?", (self.idx,))
        return publ[0][0].split(';') if publ[0][0] else ["Публикаций не было."]

    def get_villages(self):
        db = db_utils.Database()
        villages = db.execute("SELECT villages_ids FROM expeditions WHERE expedition_id = ?",
                              (self.idx,))[0][0].split(";")
        return [sup.Village(village) for village in villages]

    def get_participants(self):
        db = db_utils.Database()
        participants = db.execute("SELECT name, affiliation, supervisor FROM participants WHERE expedition_id = ?",
                                  (self.idx,))
        final_participants = []
        for part in participants:
            name, affiliation, supervisor = part
            full_name = "%s (%s)" % (name, affiliation) if affiliation else name
            if supervisor:
                full_name += " - руководитель"
                full_name = "<b>%s</b>" % (full_name,)
            final_participants.append(full_name)
        return final_participants


class ExpeditionSeries:
    def __init__(self, series_idx):
        self.idx = series_idx
        self.if_open_russia = self.get_if_open_russia()
        self.name = self.get_series_name()
        self.description = self.get_description()
        self.photos = self.get_photos()
        self.audio = self.get_audio()
        self.text = self.get_glossed_text()
        self.expeditions = self.get_expedition()

    def get_if_open_russia(self):
        db = db_utils.Database()
        if_open_russia = db.execute("SELECT if_open_russia FROM basic_info WHERE series_id = ?", (self.idx,))
        return if_open_russia[0][0] if if_open_russia else None

    def get_series_name(self):
        db = db_utils.Database()
        name = db.execute("SELECT series_name FROM basic_info WHERE series_id = ?", (self.idx,))
        return name[0][0] if name else None

    def get_description(self):
        db = db_utils.Database()
        desc = db.execute("SELECT description FROM basic_info WHERE series_id = ?", (self.idx,))
        return desc[0][0] if desc else None

    def get_photos(self):
        db = db_utils.Database()
        photos = db.execute("SELECT photo FROM basic_info WHERE series_id = ?", (self.idx,))
        processed = [sup.Photo(photo, i) for i, photo in enumerate(photos[0][0].split(";"))] if photos else None
        if processed:
            processed[0].if_active = " active"
        return processed

    def get_audio(self):
        db = db_utils.Database()
        audio = db.execute("SELECT audio FROM basic_info WHERE series_id = ?", (self.idx,))
        return audio[0][0] if audio else None

    def get_glossed_text(self):
        db = db_utils.Database()
        transcript = db.execute("SELECT local_text FROM basic_info WHERE series_id = ?", (self.idx,))
        if not transcript[0][0]:
            return None

        transcript = transcript[0][0].split()
        glosses = db.execute("SELECT text_gloss FROM basic_info WHERE series_id = ?", (self.idx,))[0][0].split()
        translation = db.execute("SELECT text_trans FROM basic_info WHERE series_id = ?", (self.idx,))[0][0]
        i = 0

        text_table = ""
        while i < len(transcript):
            if i + 12 < len(transcript):
                text_table += """
                              <table class="table table-borderless table-sm table-responsive">
                                <tbody>
                                    <tr>""" + ''.join(["<td>%s</td>" % (t,) for t in transcript[i: i + 12]]) + \
                                    """</tr>
                                    <tr> """ + ''.join(["<td>%s</td>" % (t,) for t in glosses[i: i + 12]]) + \
                                    """</tr>
                                </tbody>
                              </table>
                              """
            else:
                text_table += """<table class="table table-borderless table-sm table-responsive">
                                <tbody>
                                    <tr>""" + ''.join(["<td>%s</td>" % (t,) for t in transcript[i: i + 12]]) + \
                                    """</tr>
                                    <tr> """ + ''.join(["<td>%s</td>" % (t,) for t in glosses[i: i + 12]]) + \
                                    """</tr>
                                    <tr>
                                <td colspan="11">""" + translation + """</td>
                                    </tr>
                                </tbody>
                              </table>
                              """
            i += 12
        return text_table

    def get_expedition(self):
        db = db_utils.Database()
        expeditions = db.execute("SELECT expedition_id FROM expeditions WHERE series_id = ?", (self.idx,))
        parsed_expeditions = [Expedition(exp_id[0], i) for i, exp_id in enumerate(expeditions)]
        return parsed_expeditions
