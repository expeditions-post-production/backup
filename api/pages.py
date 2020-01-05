from flask import Flask, render_template
from api.db_handler import db_utils
from api.utils.village_handler import Village

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
