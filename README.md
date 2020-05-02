# Discuss the purpose of this database in the context of the startup, Sparkify, and their analytical goals.

Sparkify wants to analyze the data they've been collecting songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. They'd like a Postgres database with tables designed to optimize queries on song play analysis. 

# State and justify your database schema design and ETL pipeline
It is a startup with evolving needs. The schema is kept as simple and flexible.

It is star schema Schema which uses the song and log datasets and optimized for queries on song play analysis. It is the simplest style of data mart schema and is the approach most widely used to develop data warehouses and dimensional data marts. It consists of one fact tables referencing four dimension tables.

This includes the following tables with column names:

## Fact Table
* songplays - records in log data associated with song plays i.e. records with page NextSong
** songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

## Dimension Tables
* users - users in the app
** user_id, first_name, last_name, gender, level
* songs - songs in music database
** song_id, title, artist_id, year, duration
* artists - artists in music database
** artist_id, name, location, latitude, longitude
* time - timestamps of records in songplays broken down into specific units
** start_time, hour, day, week, month, year, weekday

Data modelling is dependent on the data available. The types of data which can be inserted into the table is dependent it. For example, the userId is text and userAgent ('"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36"') does not conforms to the normal operation. Another example is longitude and latitude which is float and not co-ordinates. 
These data issues needs to be addressed in the future.

The ETL is dependent on the requirements of the business. Column selection is based on the requirements of the analytics team. New features are also generated such as weekday, week, day which can be used for doing in-depth analysis.

The process included the following steps:
#### Create Tables
* CREATE statements in sql_queries.py to create each table.
* DROP statements in sql_queries.py to drop each table if it exists.
* Run create_tables.py to create your database and tables.
* Run test.ipynb to confirm the creation of your tables with the correct columns. 

##### Make sure to click "Restart kernel" to close the connection to the database after running this notebook.

#### Build ETL Processes
Followed instructions in the etl.ipynb notebook to develop ETL processes for each table. At the end of each table section, run test.ipynb to confirm that records were successfully inserted into each table. 

##### Remember to rerun create_tables.py to reset your tables before each time you run this notebook.

#### Build ETL Pipeline
Used etl.ipynb to complete etl.py to process the entire datasets. 

##### Remember to run create_tables.py before running etl.py to reset your tables. Run test.ipynb to confirm your records were successfully inserted into each table.

## References
* # https://vladmihalcea.com/postgresql-serial-column-hibernate-identity/
* # https://stackoverflow.com/questions/8150721/which-data-type-for-latitude-and-longitude