-- Basic information about students

CREATE TABLE students (
	id serial primary key,
	first_name text,
	last_name text,
	gender text
);

INSERT INTO students (first_name, last_name, gender) 
VALUES ('Jozko', 'Mrkvicka', 'male');

INSERT INTO students (first_name, last_name, gender) 
VALUES ('Martinko', 'Klingacik', 'male');

INSERT INTO students (first_name, last_name, gender) 
VALUES ('Ruzenka', 'Sipkova', 'female');

INSERT INTO students (first_name, last_name, gender) 
VALUES ('Vendelin', 'Fazula', 'male');

INSERT INTO students (first_name, last_name, gender) 
VALUES ('Karel', 'Gott', 'male');


-- Student's postal adresses

CREATE TABLE adresses (
	student_id serial references students(id) on delete cascade,
	address text,
	city text
);

INSERT INTO adresses (address, city)
VALUES ('Cintorinska 5', 'Dolna Marikova');

INSERT INTO adresses (address, city)
VALUES ('Lesna 35', 'Horna Marikova');

INSERT INTO adresses (address, city)
VALUES ('Zamocka 1', 'Bojnice');

INSERT INTO adresses (address, city)
VALUES ('Hlavna 12', 'Brusno');

INSERT INTO adresses (address, city)
VALUES ('Hvezdni 22', 'Praha');