import psycopg2
import pandas as pd

class DatabaseCaller:
    def __init__(self, config):
        """Initialize the database connection and create tables."""
        self.conn = psycopg2.connect(
            dbname=config['dbname'],
            user=config['user'],
            password=config['password'],
            host=config['host'],
            port=config['port']
        )

    def getSongs(self):
        command = "SELECT track_name FROM track_details"
        with self.conn.cursor() as cursor:
            cursor.execute(command)
            # Fetch all the rows from the result set
            rows = cursor.fetchall()
            # Extracting just the track names from the result set
            track_names = [row[0] for row in rows]
            
            # Convert to DataFrame
            df = pd.DataFrame(track_names, columns=['Track Name'])
            return df

    def close(self):
        """Close the database connection."""
        self.conn.close()

