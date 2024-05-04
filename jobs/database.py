import psycopg2
from psycopg2 import sql

class DatabaseManager:
    def __init__(self, config):
        """Initialize the database connection and create tables."""
        self.conn = psycopg2.connect(
            dbname=config['dbname'],
            user=config['user'],
            password=config['password'],
            host=config['host'],
            port=config['port']
        )
        self.conn.autocommit = True
        self.create_table_recommendations()
        self.create_table_tracks()

    def create_table_recommendations(self):
        command = \
            """
            CREATE TABLE IF NOT EXISTS recommendations (
            track_id VARCHAR PRIMARY KEY,
            recommended_track_1 VARCHAR,
            recommended_track_2 VARCHAR,
            recommended_track_3 VARCHAR,
            recommended_track_4 VARCHAR,
            recommended_track_5 VARCHAR,
            recommended_track_6 VARCHAR,
            recommended_track_7 VARCHAR,
            recommended_track_8 VARCHAR,
            recommended_track_9 VARCHAR,
            recommended_track_10 VARCHAR
                );
            """
        with self.conn.cursor() as cursor:
                cursor.execute(command)
         


    def create_table_tracks(self):
        command = \
            """
            CREATE TABLE IF NOT EXISTS track_details (
            track_id VARCHAR PRIMARY KEY,
            track_name VARCHAR,
            track_popularity INT,
            track_href VARCHAR,
            track_release_date DATE,
            album_id VARCHAR,
            artist0 VARCHAR,
            artist1 VARCHAR,
            artist2 VARCHAR,
            artist3 VARCHAR,
            artist4 VARCHAR,
            artist5 VARCHAR,
            artist6 VARCHAR,
            artist7 VARCHAR,
            artist8 VARCHAR,
            artist9 VARCHAR,
            artist10 VARCHAR
        );
            """
        with self.conn.cursor() as cursor:
                cursor.execute(command)
     
    def create_table_albums(self):
        command = \
            """
                    CREATE TABLE if not exists albums (
            album_id VARCHAR PRIMARY KEY,
            album_name VARCHAR,
            album_popularity INT,
            total_tracks INT,
            album_ref VARCHAR,
            album_release_date varchar,
            album_image VARCHAR,
            album_img_sm VARCHAR,
            album_img_md VARCHAR,
            album_img_lg VARCHAR
        );
            """
        with self.conn.cursor() as cursor:
                cursor.execute(command)
     
    def create_table_artists(self):
        command = \
            """
            CREATE TABLE if not exists artists (
            artist_id VARCHAR PRIMARY KEY,
            artist_name VARCHAR,
            genres TEXT[],
            artist_popularity INT,
            artist_followers INT,
            artist_profile VARCHAR,
            image VARCHAR,
            lg_image VARCHAR,
            md_image VARCHAR,
            sm_image VARCHAR
        );
            """
        with self.conn.cursor() as cursor:
                cursor.execute(command)
     
    def create_table_audio_features(self):
        command = \
            """
            CREATE TABLE if not exists audio_features (
            af_track_id VARCHAR PRIMARY KEY,
            af_danceability DECIMAL,
            af_energy DECIMAL,
            af_loudness DECIMAL,
            af_mode INT,
            af_acousticness DECIMAL,
            af_instrumentalness DECIMAL,
            af_liveness DECIMAL,
            af_valence DECIMAL,
            af_tempo DECIMAL,
            af_key INT,
            af_speechiness DECIMAL,
            af_time_signature INT,
            af_duration_ms INT
        );
            """
        with self.conn.cursor() as cursor:
                cursor.execute(command)
         
    def insert_data(self, table, data):
        """Insert data into the table."""
        # Assuming data is a list of tuples corresponding to the table columns
        with self.conn.cursor() as cursor:
            placeholders = ', '.join(['%s'] * len(data[0]))  # create placeholders
            query = sql.SQL('INSERT INTO {} VALUES ({})').format(
                sql.Identifier(table),
                sql.SQL(placeholders)
            )
            cursor.executemany(query, data)
            self.conn.commit()

    def close(self):
        """Close the database connection."""
        self.conn.close()


