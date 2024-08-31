CREATE KEYSPACE IF NOT EXISTS weather WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};

CREATE TABLE IF NOT EXISTS weather.weather_data (
    city_id int,
    city_name text,
    temperature float,
    humidity int,
    weather_description text,
    timestamp timestamp,
    PRIMARY KEY (city_id, timestamp)
);