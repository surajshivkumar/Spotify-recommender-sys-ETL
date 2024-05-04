from database import DatabaseManager
import pandas as pd
#warnings.filterwarnings("ignore")

import json

def load_config(config_path):
    """Load the ETL configuration file."""
    with open(config_path, 'r') as file:
        config = json.load(file)
    return config

base_dir = '../'
# config = load_config(base_dir + 'configs/etl_config.json')
config_db = load_config(base_dir + 'db/db_config.json')


def main():
    recommed_df = pd.read_csv('../data/output/recommendations_.csv')
    tracks_df = pd.read_csv('../data/output/tracks.csv')
    print(tracks_df.columns)
    dBConfig = config_db["spotify_db"]
    loader_sql = DatabaseManager(dBConfig)
#    loader_sql.insert_data(dBConfig["table_recommendation"], recommed_df.fillna(0).values)
    loader_sql.insert_data(dBConfig["table_tracks"], tracks_df.fillna(0).values)


if __name__ == "__main__":
    main()
