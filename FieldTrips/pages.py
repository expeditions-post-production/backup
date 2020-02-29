from flask import Flask, render_template
from FieldTrips.db_handler import db_utils
from FieldTrips.utils.village_handler import Village
from FieldTrips.utils.expedition_handler import ExpeditionSeries
from FieldTrips.utils.search_handler import SearchInfo
from FieldTrips.utils.support_structures import DirectionContent

app = Flask(__name__)


@app.context_processor
def set_directions():
    db = db_utils.Database()
    series = db.execute("SELECT direction FROM basic_info")
    series_set = []
    mentioned = []
    for s in series:
        if s[0] not in mentioned:
            mentioned.append(s[0])
            series_set.append(DirectionContent(s[0]))
    return dict(directions=series_set)


@app.route("/")
def index():
    db = db_utils.Database()
    villages_idxs = db.execute("SELECT village_id FROM villages")
    villages_info = [Village(idx[0]) for idx in villages_idxs]
    series = db.execute("SELECT direction FROM basic_info")
    series_set = []
    mentioned = []
    for s in series:
        if s[0] not in mentioned:
            mentioned.append(s[0])
            series_set.append(DirectionContent(s[0]))
    return render_template("index.html", villages=villages_info, directions=series_set)


@app.route("/contacts")
def contacts():
    return render_template("contacts.html")


@app.route("/exp_search")
def expedition_search():
    expeditions = SearchInfo().expeditions
    return render_template("exp_search.html", expeditions=expeditions)


@app.route("/villages/<village_idx>")
def village_info(village_idx):
    village = Village(village_idx)
    return render_template("village.html", village=village)


@app.route("/expedition/<series_idx>")
def expedition_info(series_idx):
    expedition = ExpeditionSeries(series_idx)
    return render_template("expedition.html", expedition=expedition)
