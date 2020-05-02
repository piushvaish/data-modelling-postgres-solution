# psycopg.org/docs/ -- documentation
# DROP TABLES if exists
songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES
# Fact Table
songplay_table_create = ("""

CREATE TABLE IF NOT EXISTS songplays(
songplay_id int PRIMARY KEY,
start_time timestamp,
user_id text,
level text,
artist_id text,
song_id text,
session_id int,
location text,
user_agent text)   

""")

# Dimension Table
user_table_create = ("""

CREATE TABLE IF NOT EXISTS users(
user_id text  PRIMARY KEY NOT NULL,
first_name text NOT NULL,
last_name text NOT NULL,
gender text,
level text)

""")

song_table_create = ("""

CREATE TABLE IF NOT EXISTS songs(
song_id text PRIMARY KEY NOT NULL,
title text,
artist_id text NOT NULL,
year int,
duration float)

""")

# column "lattitude" is of type point but expression is of type double precision
artist_table_create = ("""

CREATE TABLE IF NOT EXISTS artists(
artist_id text PRIMARY KEY NOT NULL,
name text,
location text,
lattitude float,
longitude float)

""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time(
start_time timestamp PRIMARY KEY NOT NULL,
hour int,
day int,
week int,
month int,
year int,
weekday int)

""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays (songplay_id, start_time, user_id,level, artist_id,song_id, session_id, location, user_agent)     
VALUES
(%s, %s, %s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (songplay_id) DO NOTHING
""")

user_table_insert = ("""
INSERT INTO users(user_id, first_name, last_name, gender,level)
VALUES
(%s, %s, %s, %s, %s)
ON CONFLICT (user_id) 
DO UPDATE SET 
first_name = EXCLUDED.first_name, 
last_name = EXCLUDED.last_name,
gender = EXCLUDED.gender, 
level = EXCLUDED.level

""")

song_table_insert = ("""
INSERT INTO songs(song_id, title, artist_id, year, duration)
VALUES
(%s, %s, %s, %s, %s)
ON CONFLICT (song_id) 
DO UPDATE SET 
title = EXCLUDED.title, 
artist_id = EXCLUDED.artist_id,
year = EXCLUDED.year, 
duration = EXCLUDED.duration
""")

artist_table_insert = ("""
INSERT INTO  artists(artist_id, name,location,lattitude, longitude)
VALUES(%s, %s, %s, %s, %s)
ON CONFLICT (artist_id) 
DO UPDATE SET 
name = EXCLUDED.name, 
location = EXCLUDED.location,
lattitude = EXCLUDED.lattitude, 
longitude = EXCLUDED.longitude

""")

time_table_insert = ("""
INSERT INTO time(start_time,hour,day,week,month, year,weekday)
VALUES
(%s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (start_time) DO NOTHING
""")

## Implement the song_select query in sql_queries.py to find the song ID and artist ID based on the title, artist name, and duration of a song.

song_select = ("""

SELECT 
s.song_id, a.artist_id
FROM songs s
INNER JOIN artists a ON  s.artist_id=a.artist_id
WHERE s.title=%s AND a.name=%s;

""")

# QUERY LISTS
create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]