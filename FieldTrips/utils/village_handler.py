from FieldTrips.db_handler import db_utils
from FieldTrips.utils import support_structures as sup


class Education:
    def __init__(self, idx):
        self.idx = idx
        self.if_school = self.get_school()
        self.if_children_garden = self.get_children_garden()
        self.school_type = self.get_school_type()
        self.school_population = self.get_school_population()
        self.school_opening = self.get_school_opening()
        self.higher_school_year = self.get_higher_school_year()
        self.boarding = self.get_boarding()
        self.higher_school_closed = self.get_higher_school_closed()
        self.where_higher_school = self.get_where_higher_school()
        self.another_school_changes = self.get_another_school_changes()
        self.alien_children = self.get_alien_children()
        self.study_langs = self.get_study_langs()
        self.writting_langs = self.get_writting_langs()
        self.langs_difference = self.get_langs_difference()
        self.first_newcomers = self.get_first_newcomers()
        self.where_newcomers_from = self.get_where_newcomers_from()
        self.tv = self.get_tv()

    def get_school(self):
        db = db_utils.Database()
        if_school = db.execute("SELECT if_school FROM villages WHERE village_id = ?", (self.idx,))
        return if_school[0][0] if if_school[0][0] else None

    def get_children_garden(self):
        db = db_utils.Database()
        if_children_garden = db.execute("SELECT children_garden_lang FROM villages WHERE village_id = ?", (self.idx,))
        return if_children_garden[0][0] if if_children_garden[0][0] else None

    def get_school_type(self):
        db = db_utils.Database()
        school_population = db.execute("SELECT school_population FROM villages WHERE village_id = ?", (self.idx,))
        return school_population[0][0] if school_population[0][0] else None

    def get_school_population(self):
        db = db_utils.Database()
        school_type = db.execute("SELECT school_type FROM villages WHERE village_id = ?", (self.idx,))
        return school_type[0][0] if school_type[0][0] else None

    def get_school_opening(self):
        db = db_utils.Database()
        school_open = db.execute("SELECT school_opening_date FROM villages WHERE village_id = ?", (self.idx,))
        return school_open[0][0] if school_open[0][0] else None

    def get_higher_school_year(self):
        db = db_utils.Database()
        higher_school_year = db.execute("SELECT higher_school_openning FROM villages WHERE village_id = ?", (self.idx,))
        return higher_school_year[0][0] if higher_school_year else None

    def get_boarding(self):
        db = db_utils.Database()
        boarding = db.execute("SELECT if_boarding_school FROM villages WHERE village_id = ?", (self.idx,))
        return boarding[0][0] if boarding[0][0] else None

    def get_higher_school_closed(self):
        db = db_utils.Database()
        closed = db.execute("SELECT if_higher_school_closed FROM villages WHERE village_id = ?", (self.idx,))
        return closed[0][0] if closed[0][0] else None

    def get_where_higher_school(self):
        db = db_utils.Database()
        where_higher_school = db.execute("SELECT where_higher_school FROM villages WHERE village_id = ?", (self.idx,))
        return where_higher_school[0][0] if where_higher_school[0][0] else None

    def get_another_school_changes(self):
        db = db_utils.Database()
        changes = db.execute("SELECT other_school_changes FROM villages WHERE village_id = ?", (self.idx,))
        return changes[0][0] if changes[0][0] else None

    def get_alien_children(self):
        db = db_utils.Database()
        children = db.execute("SELECT other_villages_in_school FROM villages WHERE village_id = ?", (self.idx,))
        return children[0][0] if children[0][0] else None

    def get_study_langs(self):
        db = db_utils.Database()
        langs = db.execute("SELECT school_languages FROM villages WHERE village_id = ?", (self.idx,))
        return langs[0][0].split(";") if langs[0][0] else None

    def get_writting_langs(self):
        db = db_utils.Database()
        langs = db.execute("SELECT school_literacy FROM villages WHERE village_id = ?", (self.idx,))
        return langs[0][0].split(";") if langs[0][0] else None

    def get_langs_difference(self):
        db = db_utils.Database()
        langs = db.execute("SELECT local_lang_learning FROM villages WHERE village_id = ?", (self.idx,))
        return langs[0][0] if langs[0][0] else None

    def get_first_newcomers(self):
        db = db_utils.Database()
        first = db.execute("SELECT first_teachers_newcomers FROM villages WHERE village_id = ?", (self.idx,))
        return first[0][0] if first[0][0] else None

    def get_where_newcomers_from(self):
        db = db_utils.Database()
        where_newcomers_from = db.execute("SELECT where_newcomers_from FROM villages WHERE village_id = ?", (self.idx,))
        return where_newcomers_from[0][0] if where_newcomers_from[0][0] else None

    def get_tv(self):
        db = db_utils.Database()
        tv = db.execute("SELECT village_television FROM villages WHERE village_id = ?", (self.idx,))
        return tv[0][0] if tv[0][0] else None


class Contacts:
    def __init__(self, idx):
        self.idx = idx
        self.another_langs = self.get_another_langs()
        self.contact_idioms = self.get_contact_idioms()
        self.markets = self.get_markets()
        self.road = self.get_road()
        self.cattle = self.get_cattle()
        self.several_idioms = self.get_several_idioms()
        self.bilinguism = self.get_biling()
        self.russian_understanding_age = self.get_russian_understanding()
        self.russian_speaking_age = self.get_russian_speaking()
        self.wife_lang = self.get_wife_lang()

    def get_another_langs(self):
        db = db_utils.Database()
        langs = db.execute("SELECT previous_languages FROM villages WHERE village_id = ?", (self.idx,))
        return langs[0][0].split(";") if langs[0][0] else None

    def get_contact_idioms(self):
        db = db_utils.Database()
        contacts = db.execute("SELECT contact_idioms FROM villages WHERE village_id = ?", (self.idx,))
        return contacts[0][0].split(";") if contacts[0][0] else None

    def get_markets(self):
        db = db_utils.Database()
        markets = db.execute("SELECT lingua_franca_market FROM villages WHERE village_id = ?", (self.idx,))
        return markets[0][0] if markets[0][0] else None

    def get_road(self):
        db = db_utils.Database()
        road = db.execute("SELECT lingua_franca_road FROM villages WHERE village_id = ?", (self.idx,))
        return road[0][0] if road[0][0] else None

    def get_cattle(self):
        db = db_utils.Database()
        cattle = db.execute("SELECT lingua_franca_cattle FROM villages WHERE village_id = ?", (self.idx,))
        return cattle[0][0] if cattle[0][0] else None

    def get_several_idioms(self):
        db = db_utils.Database()
        several_idioms = db.execute("SELECT if_polilinguism FROM villages WHERE village_id = ?", (self.idx,))
        return several_idioms[0][0].split(";") if several_idioms[0][0] else None

    def get_biling(self):
        db = db_utils.Database()
        biling = db.execute("SELECT polilinguism_frec FROM villages WHERE village_id = ?", (self.idx,))
        return biling[0][0] if biling[0][0] else None

    def get_russian_understanding(self):
        db = db_utils.Database()
        age = db.execute("SELECT russian_understanding_age FROM villages WHERE village_id = ?", (self.idx,))
        return age[0][0] if age[0][0] else None

    def get_russian_speaking(self):
        db = db_utils.Database()
        age = db.execute("SELECT russian_speaking_age FROM villages WHERE village_id = ?", (self.idx,))
        return age[0][0] if age[0][0] else None

    def get_wife_lang(self):
        db = db_utils.Database()
        wife = db.execute("SELECT wife_language FROM villages WHERE village_id = ?", (self.idx,))
        return wife[0][0] if wife[0][0] else None


class Idiom:
    def __init__(self, idx):
        self.idx = idx
        self.freq_idioms = self.get_freq_idioms()
        self.local_idiom = self.get_local_idioms()
        self.ages_of_idiom = self.get_ages()
        self.idiom_spread = self.get_idiom_spread()

    def get_freq_idioms(self):
        db = db_utils.Database()
        frecs = db.execute("SELECT idioms FROM villages WHERE village_id = ?", (self.idx,))
        return frecs[0][0].split(";") if frecs[0][0] else None

    def get_local_idioms(self):
        db = db_utils.Database()
        local_idioms = db.execute("SELECT local_idiom FROM villages WHERE village_id = ?", (self.idx,))
        return local_idioms[0][0] if local_idioms[0][0] else None

    def get_ages(self):
        db = db_utils.Database()
        ages = db.execute("SELECT idiom_ages FROM villages WHERE village_id = ?", (self.idx,))
        return ages[0][0] if ages[0][0] else None

    def get_idiom_spread(self):
        db = db_utils.Database()
        spread = db.execute("SELECT local_idiom_spread FROM villages WHERE village_id = ?", (self.idx,))
        return spread[0][0] if spread[0][0] else None


class Population:
    def __init__(self, idx):
        self.idx = idx
        self.current_value = self.get_current_value()
        self.chronology = self.get_population_chronology()
        self.ethnos = self.get_ethnos()
        self.why_ethnos = self.get_why_ethnos()
        self.neighbours = self.get_neighbours()
        self.mixed_families = self.get_mixed_families()

    def get_current_value(self):
        db = db_utils.Database()
        curr_pop = db.execute("SELECT population FROM villages WHERE village_id = ?", (self.idx,))
        return curr_pop[0][0] if curr_pop[0][0] else None

    def get_population_chronology(self):
        db = db_utils.Database()
        before_pop = db.execute("SELECT population_before FROM villages WHERE village_id = ?", (self.idx,))
        return before_pop[0][0].split(";") if before_pop[0][0] else None

    def get_ethnos(self):
        db = db_utils.Database()
        ethnos = db.execute("SELECT ethnos FROM villages WHERE village_id = ?", (self.idx,))
        return ethnos[0][0].split(";") if ethnos[0][0] else None

    def get_why_ethnos(self):
        db = db_utils.Database()
        poliethnic = db.execute("SELECT poliethnic_reasons FROM villages WHERE village_id = ?", (self.idx,))
        return poliethnic[0][0] if poliethnic[0][0] else None

    def get_neighbours(self):
        db = db_utils.Database()
        neighbours = db.execute("SELECT neighbour_idiom_villages FROM villages WHERE village_id = ?", (self.idx,))
        return neighbours[0][0].split(";") if neighbours[0][0] else None

    def get_mixed_families(self):
        db = db_utils.Database()
        mixed = db.execute("SELECT mixed_families_before FROM villages WHERE village_id = ?", (self.idx,))
        return mixed[0][0] if mixed[0][0] else None


class Village:
    def __init__(self, village_id):
        self.idx = village_id
        self.name = self.get_name()
        self.coords = self.get_coordinates()
        self.region = self.get_region()
        self.river = self.get_river()
        self.expeditions = self.get_expeditions()
        self.population = Population(self.idx)
        self.idioms = Idiom(self.idx)
        self.contacts = Contacts(self.idx)
        self.education = Education(self.idx)

    def get_name(self):
        db = db_utils.Database()
        name = db.execute("SELECT name_rus, name_latin, name_local FROM villages WHERE village_id = ?", (self.idx,))
        return sup.Name(name[0])

    def get_coordinates(self):
        db = db_utils.Database()
        coords = db.execute("SELECT coordinates FROM villages WHERE village_id = ?", (self.idx,))
        return sup.Coordinates(coords[0])

    def get_region(self):
        db = db_utils.Database()
        region = db.execute("SELECT region FROM villages WHERE village_id = ?", (self.idx,))
        region_before = db.execute("SELECT region_before FROM villages WHERE village_id = ?", (self.idx,))
        return region[0][0] + "(%s)" % (region_before[0][0],) if region_before[0][0] else region[0][0]

    def get_river(self):
        db = db_utils.Database()
        river = db.execute("SELECT river FROM villages WHERE village_id = ?", (self.idx,))
        return river[0][0] if river[0][0] else None

    def get_expeditions(self):
        db = db_utils.Database()
        series = db.execute("SELECT series_ids FROM villages WHERE village_id = ?", (self.idx,))
        series_list = series[0][0].split(";") if series[0][0] else []
        return [sup.ExpSeries(idx) for idx in series_list]