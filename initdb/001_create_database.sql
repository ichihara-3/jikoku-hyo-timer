CREATE DATABASE transportation ENCODING = UTF8;

\connect transportation

CREATE TABLE timetables (
  id SERIAL,
  station_id INT,
  line_id INT,
  train_schedule_type_id INT,
  direction_id INT,
  destination_id INT,
  departure_time TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE(station_id, line_id, train_schedule_type_id, direction_id, destination_id, departure_time)
);

