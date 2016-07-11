-- Check how many clients are duplicated
select client_id from (
	select client_id, count(*) as n from clients
	group by client_id
	order by n desc)x
where n > 1;

-- Look at dupliacte client ids - seems the space in the client
-- name is sometimes doubled
select * from clients
where client_id in (
	select client_id from (
	select client_id, count(*) as n from clients
	group by client_id
	order by n desc)x
	where n > 1);

-- Remove double spaces
update clients set client_name = replace(client_name, '  ', ' ');

-- Deduplicate
create table clients_dedupe as
select client_id, min(client_name) as client_name
from clients
group by client_id;
ALTER TABLE clients_dedupe ADD PRIMARY KEY (client_id);