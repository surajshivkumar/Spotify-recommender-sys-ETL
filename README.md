# Spotify-recommender-sys-ETL

## Flow/Plan
<pre>
  +------------------+   +---------------+   +------------------+  +------------------------+
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
