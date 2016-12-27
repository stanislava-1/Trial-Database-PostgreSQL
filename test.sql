-- Basic information about students

CREATE TABLE students (
	id serial primary key,
	first_name text,
	last_name text,
	gender text,
	country text
);

INSERT INTO students (first_name, last_name, gender, country) 
VALUES ('Jožko', 'Mrkvička', 'male', 'Slovakia');

INSERT INTO students (first_name, last_name, gender, country) 
VALUES ('Martinko', 'Klingáčik', 'male', 'Slovakia');

INSERT INTO students (first_name, last_name, gender, country) 
VALUES ('Svatopluk', 'Kuřátko', 'male', 'Czech Republic');

INSERT INTO students (first_name, last_name, gender, country) 
VALUES ('Ruženka', 'Šípková', 'female', 'Slovakia');

INSERT INTO students (first_name, last_name, gender, country) 
VALUES ('Vendelín', 'Fazuľa', 'male', 'Slovakia');

INSERT INTO students (first_name, last_name, gender, country) 
VALUES ('Josef', 'Švejk', 'male', 'Czech Republic');

INSERT INTO students (first_name, last_name, gender, country) 
VALUES ('Maruška', 'Jahodová', 'female', 'Slovakia');

INSERT INTO students (first_name, last_name, gender, country) 
VALUES ('Sandokan', 'Dlhovlasý', 'male', 'Malaysia');

INSERT INTO students (first_name, last_name, gender, country) 
VALUES ('Pipi', 'Dlhopančuchová', 'female', 'Sweden');

INSERT INTO students (first_name, last_name, gender, country) 
VALUES ('Janka', 'Tárajka', 'female', 'Slovakia');

INSERT INTO students (first_name, last_name, gender, country) 
VALUES ('Janko', 'Hraško', 'male', 'Slovakia');

