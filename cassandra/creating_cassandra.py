CREATE KEYSPACE foo
  WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 };

create table foo.users (
	col1 text PRIMARY KEY,
	col2 list<text>
	);

# CREATE KEYSPACE bar
#   WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 };

# drop table if exists users;
# drop type if exists date1;
# drop type if exists address;
# drop type if exists grades;

# CREATE type bar.date1(
# 	date1 bigint
# 	);
# CREATE type bar.address(
# 	building text,
# 	coord tuple<double,double>,
# 	street text,
# 	zipcode text);

# CREATE type bar.grades(
# 	date FROZEN<date1>,
# 	grade text,
# 	score int
# 	);

# create table bar.users (
# 	id text PRIMARY KEY,
# 	address FROZEN<address>,
# 	borough text,
# 	cuisine text,
# 	grades list<FROZEN<grades>>,
# 	name text,
# 	restaurant_id text
# 	);

# address
# 	building
# 	coord
# 	street
# 	zipcode
# borough
# cuisine
# grades
# 	date
# 		$date
# 	grade
# 	score
# name
# restaurant_id

# insert into users json '{"id":"user0", "address": {"building": "1007", "coord": [-73.856077, 40.848447], "street": "Morris Park Ave", "zipcode": "10462"}, "borough": "Bronx", "cuisine": "Bakery", "grades": [{"date": {"date1": 1393804800000}, "grade": "A", "score": 2}, {"date": {"date1": 1378857600000}, "grade": "A", "score": 6}, {"date": {"date1": 1358985600000}, "grade": "A", "score": 10}, {"date": {"date1": 1322006400000}, "grade": "A", "score": 9}, {"date": {"date1": 1299715200000}, "grade": "B", "score": 14}], "name": "Morris Park Bake Shop", "restaurant_id": "30075445"}';
