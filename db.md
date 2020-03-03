# databases

## transportation


### tables

#### timetables 時刻表

- id ID SERIAL: PRIMARY
- station_id 駅ID INT: FK
- line_id 路線ID INT: FK
- train_schedule_type_id ダイヤ種別ID INT: FK
- direction_id 方面ID INT: FK
- destination_id 行先ID INT: FK
- departure_time 時刻 TIMESTAMP

UNIQUE(駅ID, 路線ID, ダイヤ種別ID, 方面ID, 行先ID, 時刻)

#### stations 駅

- id ID SERIAL: PRIMARY
- name 駅名 VARCHAR(255)
- railway_operator_id 鉄道事業者ID: FK

#### railway_operators 鉄道事業者

- id ID SERIAL: PRIMARY
- name 鉄道事業者名 VARCHAR(255)

#### directions 方面

- id ID SERIAL: PRIMARY
- name VARCHAR(255)

#### destinations 行先

- id ID SERIAL: PRIMARY
- name 行先名 VARCHAR(255)

#### lines 路線種別

- id ID SERIAL: PRIMARY
- name 路線名 VARCHAR(255)
- railway_operator_id 鉄道事業者ID INT: FK

### train_schedule_types ダイヤ種別

- id ID SERIAL: PRIMARY
- train_schedule_type ダイヤ種別 VARCHAR(255): 平日・土休日・その他など

