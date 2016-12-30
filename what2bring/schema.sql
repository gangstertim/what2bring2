drop table if exists events;
create table events (
  id integer primary key autoincrement,
  eventName text not null,
  name text not null
);
