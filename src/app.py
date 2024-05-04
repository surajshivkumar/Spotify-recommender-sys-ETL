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
    print(songs.columns)
    songs = songs['Track Name'].unique().tolist()
    return render_template("search.html",songs = songs)

<<<<<<< HEAD

# @app.route("/recommend")
# def dashboard():
#     return render_template("dashboard.html")

=======
# @app.route("/recommend")
# def dashboard():
#     return render_template("dashboard.html")

>>>>>>> bf4c7c01a4cf52f3ed30bfcf00e8d6be4d5f5a7d
@app.route("/results",methods=['POST'])
def results():
    '''
    Endpoint that handles the search functionality and displays results.
    '''
    if request.method == 'POST':
        searchTerm = request.form.get('search-term')
        #db search logic below
<<<<<<< HEAD
        results = ['test']
=======
        results = [
            {
							'name': 'Blank Space',
							'imgUrl': 'https://github.com/ecemgo/mini-samples-great-tricks/assets/13468728/ea61baa7-9c4b-4f43-805e-81de5fc8aa2b',
							'artistName': 'Taylor Swift',
							'timeStamp': '4:33'
            },
						{
							'name': 'Blank Space',
							'imgUrl': 'https://github.com/ecemgo/mini-samples-great-tricks/assets/13468728/ea61baa7-9c4b-4f43-805e-81de5fc8aa2b',
							'artistName': 'Taylor Swift',
							'timeStamp': '4:33'
            },
						{
							'name': 'Blank Space',
							'imgUrl': 'https://github.com/ecemgo/mini-samples-great-tricks/assets/13468728/ea61baa7-9c4b-4f43-805e-81de5fc8aa2b',
							'artistName': 'Taylor Swift',
							'timeStamp': '4:33'
            }
        ]
>>>>>>> bf4c7c01a4cf52f3ed30bfcf00e8d6be4d5f5a7d
        return render_template('dashboard.html', results=results)



if __name__ == "__main__":
    app.run(debug=True, port=5002,threaded=False)