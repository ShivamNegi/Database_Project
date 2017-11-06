CREATE KEYSPACE foo
  WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 };

create table foo.users (
	col1 text PRIMARY KEY,
	col2 list<text>
	);

