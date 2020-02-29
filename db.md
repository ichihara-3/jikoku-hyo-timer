# databases

## transportation


### tables

#### timetables 時刻表

- ID SERIAL: PRIMARY
- 駅ID INT: FK
- 路線ID INT: FK
- ダイヤ種別ID INT: FK
- 方面ID INT: FK
- 行先ID INT: FK
- 時刻 TIMESTAMP

UNIQUE(駅ID, 路線ID, ダイヤ種別ID, 方面ID, 行先ID, 時刻)

#### stations 駅

- ID SERIAL: PRIMARY
- 駅名 VARCHAR(255)
- 鉄道事業者ID: FK

#### railway_operators 鉄道事業者

- ID SERIAL: PRIMARY
- 鉄道事業者名 VARCHAR(255)

#### directions 方面

- ID SERIAL: PRIMARY
- 方面名 VARCHAR(255)

#### destinations 行先

- ID SERIAL: PRIMARY
- 行先名 VARCHAR(255)

#### lines 路線種別

- ID SERIAL: PRIMARY
- 路線名 VARCHAR(255)
- 鉄道事業者ID INT: FK

### train_schedule_types

- ID SERIAL: PRIMARY
- ダイヤ種別 VARCHAR(255): 平日・土休日・その他など

