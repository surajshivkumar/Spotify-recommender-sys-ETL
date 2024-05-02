import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from tqdm import tqdm
import pandas as pd

class APIExtractor:
    def __init__(self, client_id, client_secret):
        client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
        self.sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    def get_audio_features(self, track_id):
        features = self.sp.audio_features(track_id)[0]
        return {
            'af_track_id': features['id'],
            'af_danceability': features.get('danceability'),
            'af_energy': features.get('energy'),
            'af_loudness': features.get('loudness'),
            'af_mode': features.get('mode'),
            'af_acousticness': features.get('acousticness'),
            'af_instrumentalness': features.get('instrumentalness'),
            'af_liveness': features.get('liveness'),
            'af_valence': features.get('valence'),
            'af_tempo': features.get('tempo'),
            'af_key': features.get('key'),
            'af_speechiness': features.get('speechiness'),
            'af_time_signature': features.get('time_signature'),
            'af_duration_ms': features.get('duration_ms')
        }

    def get_track_info(self, track_id):
        track_info = self.sp.track(track_id)
        track = {
            'track_id': track_info['id'],
            'track_name': track_info['name'],
            'track_popularity': track_info['popularity'],
            'track_href': track_info['external_urls']['spotify'],
            'track_release_date': track_info['album']['release_date'],
            'album_id': track_info['album']['id'],
            'artists': [artist['id'] for artist in track_info['artists']]
        }
        return track

    def get_album_info(self, album_id):
        album_info = self.sp.album(album_id)
        album = {
            'album_id': album_info['id'],
            'album_name': album_info['name'],
            'album_popularity': album_info['popularity'],
            'total_tracks': album_info['total_tracks'],
            'album_ref': album_info['external_urls']['spotify'],
            'album_release_date': album_info['release_date'],
            'album_images': {size: img['url'] for size, img in zip(['sm', 'md', 'lg'], album_info['images'])}
        }
        return album

    def get_artist_info(self, artist_id):
        artist_info = self.sp.artist(artist_id)
        artist = {
            'artist_id': artist_info['id'],
            'artist_name': artist_info['name'],
            'genres': artist_info['genres'],
            'artist_popularity': artist_info['popularity'],
            'artist_followers': artist_info['followers']['total'],
            'artist_profile': artist_info['external_urls']['spotify'],
            'images': {size: img['url'] for size, img in zip(['sm', 'md', 'lg'], artist_info['images'])}
        }
        return artist
    
    
def chunker(seq, size):
    """Chunk a list into specified sizes."""
    return [seq[i:i + size] for i in range(0, len(seq), size)]

def main():
    # Assume df2 is a DataFrame already loaded with track IDs
    chunked_tracks = chunker(tracks.track_id.unique(), 50)
    
    extractor = APIExtractor('your_client_id', 'your_client_secret')

    # Fetch and process audio features for tracks
    track_audio_features = []
    for track_ids in tqdm(chunked_tracks, desc='Processing Tracks'):
        batch_audio_feat = extractor.sp.audio_features(track_ids)
        for af in batch_audio_feat:
            track_audio_features.append(extractor.get_audio_features(af))

    # Process artist information
    artists = list(set([j for i in df2[['artist0', 'artist1', 'artist2', 'artist3', 'artist4', 'artist5', 'artist6', 'artist7', 'artist8', 'artist9', 'artist10']].values for j in i if j is not None]))[1:]
    artists_chunked = chunker(artists, 50)
    
    artist_details = []
    for art_ids in tqdm(artists_chunked, desc='Processing Artists'):
        batch_artists = extractor.sp.artists(art_ids)
        for art in batch_artists['artists']:
            artist_details.append(extractor.get_artist_info(art))

    # Save artists data to CSV
    pd.DataFrame(artist_details).to_csv('artists.csv', index=False)

    # Process and save album information
    album_ids = df2.album_id.unique()
    album_chunks = chunker(album_ids, 20)
    
    albums = []
    for alb_ids in tqdm(album_chunks, desc='Processing Albums'):
        album_data_batch = extractor.sp.albums(alb_ids)
        for album_info in album_data_batch['albums']:
            albums.append(extractor.get_album_info(album_info))
    
    # Create DataFrame and remove unwanted columns
    albums_df = pd.DataFrame(albums)
    albums_df = albums_df.drop(columns=['genres'])
    albums_df.to_csv('albums.csv', index=False)

