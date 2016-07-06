SET client_encoding = 'UTF8';

drop table if exists town_state;
create table town_state (
  store_id text,
  town text,
  state text);
\copy town_state from 'raw/town_state.csv' with (format csv, delimiter ',', header TRUE)

drop table if exists clients;
create table clients (
  client_id text,
  client_name text);
\copy clients from 'raw/cliente_tabla.csv' with (format csv, delimiter ',', header TRUE)

drop table if exists products;
create table products (
  product_id text,
  product_name text);
\copy products from 'raw/producto_tabla.csv' with (format csv, delimiter ',', header TRUE)

drop table if exists products;
create table products (
  product_id text,
  product_name text);
\copy products from 'raw/producto_tabla.csv' with (format csv, delimiter ',', header TRUE)

drop table if exists test;
create table test (
  id int,
  week int,
  store_id text,
  channel_id text,
  route_id text,
  client_id text,
  product_id text
  );
\copy test from 'raw/test.csv' with (format csv, delimiter ',', header TRUE)

drop table if exists train;
create table train (
  week int,
  store_id text,
  channel_id text,
  route_id text,
  client_id text,
  product_id text,
  sales_vol int,
  sales_val decimal(9,2),
  returns_vol int,
  returns_val decimal(9,2),
  demand int
  );
\copy train from 'raw/train.csv' with (format csv, delimiter ',', header TRUE)

create index on train(week);
create index on train(store_id);
create index on train(channel_id);
create index on train(route_id);
create index on train(client_id);
create index on train(product_id);
