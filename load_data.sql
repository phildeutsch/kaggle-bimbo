SET client_encoding = 'UTF8';

drop table if exists town_state;

create table town_state (
  store_id text,
  town text,
  state text);

\copy town_state from 'raw/town_state.csv' with (format csv, delimiter ',')
