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

-- Information about courses

CREATE TABLE courses (
	id text primary key,
	name text,
	teacher text
);

INSERT INTO courses VALUES ('C001', 'History', 'Peter Veľký');

INSERT INTO courses VALUES ('C002', 'Mathematics', 'Albert Einzwei');

INSERT INTO courses VALUES ('C003', 'Computer Science', 'Ján Kocka');

INSERT INTO courses VALUES ('C004', 'Slovak Language', 'Anna Bystrická');

INSERT INTO courses VALUES ('C005', 'Chemistry', 'Zlatica Uhlíková');

INSERT INTO courses VALUES ('C006', 'Physics', 'Vladimír Volt');

INSERT INTO courses VALUES ('C007', 'English Language', 'John Smith');

INSERT INTO courses VALUES ('C008', 'Journalism', 'Milan Večerník');

INSERT INTO courses VALUES ('C009', 'Painting', 'Alžbeta Benková');

INSERT INTO courses VALUES ('C010', 'Music Theory', 'Eugénia Suchoňová');

INSERT INTO courses VALUES ('C011', 'Creative Writing', 'Kristián Benda');

-- Information about student's enrolments to courses

CREATE TABLE enrolments (
	student_id integer references students (id) on delete cascade,
	course_id text references courses (id) on delete cascade 
);

INSERT INTO enrolments VALUES (1, 'C002');
INSERT INTO enrolments VALUES (1, 'C003');
INSERT INTO enrolments VALUES (1, 'C007');
INSERT INTO enrolments VALUES (2, 'C001');
INSERT INTO enrolments VALUES (2, 'C009');
INSERT INTO enrolments VALUES (2, 'C011');
INSERT INTO enrolments VALUES (3, 'C005');
INSERT INTO enrolments VALUES (3, 'C006');
INSERT INTO enrolments VALUES (4, 'C002');
INSERT INTO enrolments VALUES (4, 'C003');
INSERT INTO enrolments VALUES (4, 'C006');
INSERT INTO enrolments VALUES (5, 'C004');
INSERT INTO enrolments VALUES (5, 'C008');
INSERT INTO enrolments VALUES (5, 'C011');
INSERT INTO enrolments VALUES (6, 'C001');
INSERT INTO enrolments VALUES (6, 'C009');
INSERT INTO enrolments VALUES (6, 'C010');
INSERT INTO enrolments VALUES (7, 'C001');
INSERT INTO enrolments VALUES (7, 'C004');
INSERT INTO enrolments VALUES (8, 'C005');
INSERT INTO enrolments VALUES (8, 'C006');
INSERT INTO enrolments VALUES (8, 'C007');
INSERT INTO enrolments VALUES (9, 'C002');
INSERT INTO enrolments VALUES (9, 'C005');
INSERT INTO enrolments VALUES (9, 'C006');
INSERT INTO enrolments VALUES (10, 'C007');
INSERT INTO enrolments VALUES (10, 'C009');
INSERT INTO enrolments VALUES (11, 'C008');
INSERT INTO enrolments VALUES (11, 'C011');