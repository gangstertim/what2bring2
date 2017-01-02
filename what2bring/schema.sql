drop table if exists events;
drop table if exists guests;

create table events (
  id integer primary key autoincrement,
  name text not null,
  location text,
  description text,
  datetime datetime,
  hostName text not null,
  hostEmail text not null,
  dishesToBring text,
  numGuests integer,
  dishesBeingBrought text,
  acceptCash integer not null,
  cashAmount integer,
  created_at datetime not null,
  updated_at datetime not null
);

create table guests (
  name text not null,
  email text,
  dishes text,
  bringing_cash integer,
  event_id integer not null,
  created_at datetime not null
);

CREATE UNIQUE INDEX event_id
on events (id);
