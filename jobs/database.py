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

    def create_table_recommendations(self):
        command = \
            """
            CREATE TABLE IF NOT EXISTS tracks_recommendations (
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


