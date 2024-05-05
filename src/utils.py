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
    
    def getTrackID(self,track_name):
        command = f"SELECT track_id FROM track_details where track_name = '{track_name}' order by track_popularity desc limit 1"
        with self.conn.cursor() as cursor:
            cursor.execute(command)
            # Fetch all the rows from the result set
            rows = cursor.fetchall()
            # Extracting just the track names from the result set
            track_id = [row[0] for row in rows]
            
            # Convert to DataFrame

            return track_id
    
    def getRecommendations(self,trackID):
        command = f"SELECT * FROM recommendations where track_id = '{trackID[0]}' "
        with self.conn.cursor() as cursor:
            cursor.execute(command)
            # Fetch all the rows from the result set
            rows = cursor.fetchall()
            # Extracting just the track names from the result set

            
            # Convert to DataFrame

            return rows[0]
        
    def getRecommendationTrackDetails(self,trackIDS):
        command = f"select track_name, track_href,af_duration_ms,artist_name,image from (select *,row_number() over(partition by track_name order by track_popularity desc) as rnk from track_details where track_id in {trackIDS} order by rnk) a  join (select af_track_id, af_duration_ms from audio_features) b on a.track_id = b.af_track_id join (select artist_id, artist_name,image from artists) c on a.artist0 = c.artist_id  where a.rnk=1; "
        d = pd.read_sql(command,self.conn)
        d['af_duration_ms'] = d.af_duration_ms.map(lambda x: x//60000)
        tr_details = []
        
        for idx,row in d.iterrows():
            tr = {}
            tr['name'] = row['track_name']
            tr['timeStamp'] = row['af_duration_ms']
            tr['artistName'] = row['artist_name']
            tr['imgUrl'] = row['image']
            tr_details.append(tr)
            
        return tr_details
    
        

    def close(self):
        """Close the database connection."""
        self.conn.close()

#select * from (select *,row_number() over(partition by track_name order by track_popularity desc) as rnk from track_details where track_id in ('3aLWuWKHaTV4Ok7LKvXRYn', '43lcnmBoTbTRjaer77OBf7', '1PNb8pRsZGa8XN1m5nJe70', '6gpcs5eMhJwax4mIfKDYQk', '14eXPUCqMrws746wzWKgNN', '2BgEsaKNfHUdlh97KmvFyo', '3F1mueW8iouZUgjmawhVhe', '42tFTth2jcF7iSo0RBjfJF', '4WgvTITBJbEfCJHguiE7QS', '5DsD9rUwGiiWZxyDPkm48V', '20hGTzgOu6U8WPgYg9AtXr') order by rnk) a  where a.rnk=1;

