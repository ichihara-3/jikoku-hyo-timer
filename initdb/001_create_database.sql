CREATE DATABASE transportation ENCODING = UTF8;

\connect transportation

CREATE TABLE railway_operators (
  id SERIAL NOT NULL,
  name VARCHAR(255) NOT NULL,
  PRIMARY KEY (id),
  UNIQUE (name)
);

CREATE TABLE stations (
  id SERIAL NOT NULL,
  name VARCHAR(255) NOT NULL,
  railway_operator_id INT NOT NULL REFERENCES railway_operators (id),
  PRIMARY KEY (id),
  UNIQUE (railway_operator_id, name)
);

CREATE TABLE directions (
  id SERIAL NOT NULL,
  name VARCHAR(255) NOT NULL,
  PRIMARY KEY (id),
  UNIQUE (name)
);

CREATE TABLE destinations (
  id SERIAL NOT NULL,
  name VARCHAR(255) NOT NULL,
  PRIMARY KEY (id),
  UNIQUE (name)
);

CREATE TABLE lines (
  id SERIAL NOT NULL,
  name VARCHAR(255) NOT NULL,
  railway_operator_id INT NOT NULL REFERENCES railway_operators (id),
  PRIMARY KEY (id),
  UNIQUE (railway_operator_id, name)
);

CREATE TABLE train_schedule_types (
  id SERIAL NOT NULL,
  train_schedule_type VARCHAR(255) NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE timetables (
  id SERIAL NOT NULL,
  station_id INT NOT NULL REFERENCES stations (id),
  line_id INT NOT NULL REFERENCES lines (id),
  train_schedule_type_id INT NOT NULL REFERENCES train_schedule_types (id),
  direction_id INT NOT NULL REFERENCES directions (id),
  destination_id INT NOT NULL REFERENCES destinations (id),
  departure_time TIMESTAMP NOT NULL,
  PRIMARY KEY (id),
  UNIQUE (station_id, line_id, train_schedule_type_id, direction_id, destination_id, departure_time)
);

CREATE TABLE timetables_name (
  id SERIAL NOT NULL,
  station VARCHAR(255) NOT NULL,
  line VARCHAR(255) NOT NULL,
  train_schedule_type VARCHAR(255) NOT NULL,
  direction VARCHAR(255) NOT NULL,
  destination VARCHAR(255) NOT NULL,
  departure_time TIME NOT NULL,
  PRIMARY KEY (id)
);
