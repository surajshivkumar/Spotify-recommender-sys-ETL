from flask import Flask, request, jsonify, render_template, send_from_directory

from flask_cors import CORS
import json
import pandas as pd
from utils import DatabaseCaller


def load_config(config_path):
    """Load the ETL configuration file."""
    with open(config_path, 'r') as file:
        config = json.load(file)
    return config

base_dir = '../'
# config = load_config(base_dir + 'configs/etl_config.json')
config_db = load_config(base_dir + 'db/db_config.json')

dBConfig = config_db["spotify_db"]
caller = DatabaseCaller(dBConfig)


app = Flask(__name__)




@app.route("/",methods=['GET', 'POST'])
@app.route("/home",methods=['GET', 'POST'])
def home():
    songs = caller.getSongs()
    songs = songs.values.tolist()
    return render_template("search.html",songs = songs)

@app.route("/recommend")
def dashboard():
    return render_template("dashboard.html")




if __name__ == "__main__":
    app.run(debug=True, port=5002,threaded=False)