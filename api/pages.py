from flask import Flask, render_template
from api.db_handler import db_utils
from api.utils.village_handler import Village
from api.utils.expedition_handler import ExpeditionSeries

app = Flask(__name__)


@app.route("/")
def index():
    db = db_utils.Database()
    villages_idxs = db.execute("SELECT village_id FROM villages")
    villages_info = [Village(idx[0]) for idx in villages_idxs]
    return render_template("index.html", villages=villages_info)


@app.route("/contacts")
def contacts():
    return render_template("contacts.html")


@app.route("/villages/<village_idx>")
def village_info(village_idx):
    village = Village(village_idx)
    return render_template("village.html", village=village)


@app.route("/expedition/<series_idx>")
def expedition_info(series_idx):
    expedition = ExpeditionSeries(series_idx)
    return render_template("expedition.html", expedition=expedition)
