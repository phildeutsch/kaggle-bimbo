SET client_encoding = 'UTF8';

DROP TABLE IF EXISTS town_state;
CREATE TABLE town_state (
  store_id TEXT,
  town TEXT,
  state TEXT);
\COPY town_state FROM 'raw/town_state.csv' WITH (FORMAT CSV, DELIMITER ',', HEADER TRUE)

DROP TABLE IF EXISTS clients;
CREATE TABLE clients (
  client_id TEXT,
  client_name TEXT);
\COPY clients FROM 'raw/cliente_tabla.csv' WITH (FORMAT CSV, DELIMITER ',', HEADER TRUE)

DROP TABLE IF EXISTS products;
CREATE TABLE products (
  product_id TEXT PRIMARY KEY,
  product_name TEXT);
\COPY products FROM 'raw/producto_tabla.csv' WITH (FORMAT CSV, DELIMITER ',', HEADER TRUE)

DROP TABLE IF EXISTS products;
CREATE TABLE products (
  product_id TEXT,
  product_name TEXT);
\COPY products FROM 'raw/producto_tabla.csv' WITH (FORMAT CSV, DELIMITER ',', HEADER TRUE)

DROP TABLE IF EXISTS test;
CREATE TABLE test (
  id INT,
  week INT,
  store_id TEXT,
  channel_id TEXT,
  route_id TEXT,
  client_id TEXT,
  product_id TEXT
  );
\COPY test FROM 'raw/test.csv' WITH (FORMAT CSV, DELIMITER ',', HEADER TRUE)

DROP TABLE IF EXISTS train;
CREATE TABLE train (
  week int,
  store_id TEXT,
  channel_id TEXT,
  route_id TEXT,
  client_id TEXT,
  product_id TEXT,
  sales_vol INT,
  sales_val DECIMAL(9,2),
  returns_vol INT,
  returns_val DECIMAL(9,2),
  demand INT
  );
\COPY train FROM 'raw/train.csv' WITH (FORMAT CSV, DELIMITER ',', HEADER TRUE)

CREATE INDEX ON train(week);
CREATE INDEX ON train(store_id);
CREATE INDEX ON train(channel_id);
CREATE INDEX ON train(route_id);
CREATE INDEX ON train(client_id);
CREATE INDEX ON train(product_id);

VACUUM ANALYZE train;
