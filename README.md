<h1 align = "center">Spotify's Personalized Music Recommender</h1>
<p align="center">
  
  <img src="https://cdn.dribbble.com/users/441326/screenshots/3165191/media/45c2723efdf8be2140ff43913cbe8a3f.gif" alt="Animated GIF">
</p>

Dynamically personalizes music recommendations using Spotify's rich dataset, processed through a sophisticated ETL pipeline and served via an intuitive React interface.



## Flow/Plan
<pre>
+------------------+   +---------------+   +------------------+   +------------------------+
| Spotify API      |   | Extract       |   | Transform        |   | Load                   |
| Data Source      |-->| (Data Source) |-->| (Data Cleaning)  |-->| (PostgreSQL DB with    |
+------------------+   +---------------+   +------------------+   |  Star Schema)          |
                                                                  +------------------------+
                                                                                    |
                                                                                    |
                                      +-------------------------+   +---------------v---------------+
                                      | Recommendation Engine   |   | Recommendations Table          |
                                      | (Algorithm Processing)  |   | Stored in PostgreSQL-3 cluster |
                                      +-------------------------+   +--------------------------------+
                                                                                    |
                                                              +---------------------v-------------------+
                                                              | Flask Backend                          |
                                                              | (API Endpoints for Data Interaction)   |
                                                              +----------------------------------------+
                                                                             |
                                                              +-------------v--------------+
                                                              | React Frontend             |
                                                              | (User Interface)           |
                                                              +----------------------------+
                                                                             |
                                                              +-------------v--------------+
                                                              | User Interaction           |
                                                              | (Select Favorite Song,     |
                                                              |  Receive Recommendations,  |
                                                              |  Like/Dislike)             |
                                                              +----------------------------+

</pre>


Here's a sample README for the Extract layer of your Spotify recommendation system project, focusing on how data is obtained from the Spotify API:

---

## Spotify Data Extraction Layer

### Overview
This component of the Spotify recommendation system is responsible for extracting data from the Spotify Web API. The data pertains to tracks, albums, artists, and audio features, which are essential for building a comprehensive recommendation engine.

### Data Features
The following datasets are extracted from the Spotify API:

1. **Tracks**:
   - `track_id`: The unique identifier for the track.
   - `track_name`: The name of the track.
   - `track_popularity`: Popularity score of the track.
   - `track_href`: API URL reference to the track details.
   - `track_release_date`: Release date of the track.
   - `album_id`: Associated album ID.
   - `artist0` to `artist10`: IDs for up to 11 artists associated with the track.

2. **Albums**:
   - `album_id`: The unique identifier for the album.
   - `album_name`: The name of the album.
   - `album_popularity`: Popularity score of the album.
   - `total_tracks`: Total number of tracks in the album.
   - `album_ref`: API URL reference to the album details.
   - `album_release_date`: Release date of the album.
   - `album_image`, `album_img_sm`, `album_img_md`, `album_img_lg`: Image URLs in various sizes.

3. **Artists**:
   - `artist_id`: The unique identifier for the artist.
   - `artist_name`: The name of the artist.
   - `genres`: List of genres the artist is associated with.
   - `artist_popularity`: Popularity score of the artist.
   - `artist_followers`: Number of followers the artist has.
   - `artist_profile`: API URL reference to the artist details.
   - `image`, `lg_image`, `md_image`, `sm_image`: Image URLs in various sizes.

4. **Audio Features**:
   - `af_track_id`: Track ID associated with the audio features.
   - `af_danceability`, `af_energy`, `af_loudness`, `af_mode`, `af_acousticness`, `af_instrumentalness`, `af_liveness`, `af_valence`, `af_tempo`, `af_key`, `af_speechiness`, `af_time_signature`, `af_duration_ms`: Various measurable audio features.

## Extraction Process
1. **Authorization**:
   - Obtain an access token using the Client Credentials Flow, allowing you to authenticate with the Spotify Web API.

2. **Making API Requests**:
   - Use the access token to make requests to Spotify's endpoints for tracks, albums, artists, and audio features.
   - Handle pagination to ensure complete data retrieval for datasets that span multiple pages.

3. **Data Handling**:
   - Convert JSON responses into structured formats suitable for the transformation stage.
   - Check for errors and inconsistencies during the data retrieval and log any issues encountered.




## Schema
<pre>
                                     +-------------------------+
                                     |       fact_tracks       |
                                     +-------------------------+
                                     | PK | track_id           |
                                     | FK | album_id           |
                                     | FK | artist_id          |
                                     | FK | af_track_id        |
                                     |    | track_popularity   |
                                     |    | track_release_date |
                                     +---------+---------+
                                               |
                 +-----------------------------+-----------------------------+
                 |                             |                             |
   +-------------v-----------+   +-------------v------------+   +-------------v-------------+
   |      dim_albums         |   |      dim_audio_features  |   |       dim_artists         |
   +-------------------------+   +--------------------------+   +---------------------------+
   | PK | album_id           |   | PK | af_track_id         |   | PK | artist_id            |
   |    | album_name         |   |    | af_danceability     |   |    | artist_name          |
   |    | album_popularity   |   |    | af_energy           |   |    | genres               |
   |    | total_tracks       |   |    | af_loudness         |   |    | artist_popularity    |
   |    | album_release_date |   |    | af_mode             |   |    | artist_followers     |
   |    | album_image        |   |    | af_acousticness     |   |    | artist_profile       |
   |    | album_img_sm       |   |    | af_instrumentalness |   |    | image                |
   |    | album_img_md       |   |    | af_liveness         |   |    | lg_image             |
   |    | album_img_lg       |   |    | af_valence          |   |    | md_image             |
   +-------------------------+   |    | af_tempo            |   |    | sm_image             |
                                 |    | af_key              |   +-------------+-------------+
                                 |    | af_speechiness      |                 |
                                 |    | af_time_signature   |   +-------------v-------------+
                                 |    | af_duration_ms      |   |      artist_tracks        |
                                 +--------------------------+   +---------------------------+
                                                                | FK | track_id             |
                                                                | FK | artist_id            |
                                                                +---------------------------+


</pre>
