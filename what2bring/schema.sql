drop table if exists events;
drop table if exists guests;

create table events (
  id integer primary key autoincrement,
  eventName text not null,
  eventLocation text,
  eventDescription text,
  eventDatetime integer,
  hostName text not null,
  hostEmail text not null,
  dishesToBring text,
  dishesBeingBrought text,
  acceptCash integer not null,
  cashAmount integer,
  created_at integer not null,
  updated_at integer not null
);

create table guests (
  name text not null,
  email text,
  dishes text,
  bringing_cash integer,
  event_id integer not null,
  created_at integer not null,
  updated_at integer not null
);

CREATE UNIQUE INDEX event_id
on events (id);
