-- Basic information about students

CREATE TABLE students (
	id serial primary key,
	first_name text,
	last_name text,
	birthday date,
	gender text,
	country text
);

INSERT INTO students (first_name, last_name, birthday, gender, country) 
VALUES ('Jožko', 'Mrkvička', '1980-02-21', 'male', 'Slovakia');

INSERT INTO students (first_name, last_name, birthday, gender, country)
VALUES ('Martinko', 'Klingáčik', '1965-08-08', 'male', 'Slovakia');

INSERT INTO students (first_name, last_name, birthday, gender, country) 
VALUES ('Svatopluk', 'Kuřátko', '1974-04-15', 'male', 'Czech Republic');

INSERT INTO students (first_name, last_name, birthday, gender, country)
VALUES ('Ruženka', 'Šípková', '1997-07-03', 'female', 'Slovakia');

INSERT INTO students (first_name, last_name, birthday, gender, country)
VALUES ('Vendelín', 'Fazuľa', '1990-10-18', 'male', 'Slovakia');

INSERT INTO students (first_name, last_name, birthday, gender, country)
VALUES ('Josef', 'Švejk', '1961-01-11', 'male', 'Czech Republic');

INSERT INTO students (first_name, last_name, birthday, gender, country)
VALUES ('Maruška', 'Jahodová', '1996-12-24', 'female', 'Slovakia');

INSERT INTO students (first_name, last_name, birthday, gender, country)
VALUES ('Sandokan', 'Dlhovlasý', '1985-05-06', 'male', 'Malaysia');

INSERT INTO students (first_name, last_name, birthday, gender, country)
VALUES ('Pipi', 'Pančuchová', '1998-08-30', 'female', 'Sweden');

INSERT INTO students (first_name, last_name, birthday, gender, country)
VALUES ('Janka', 'Tárajka', '1977-03-17', 'female', 'Slovakia');

INSERT INTO students (first_name, last_name, birthday, gender, country)
VALUES ('Janko', 'Hraško', '1987-09-12', 'male', 'Slovakia');

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
INSERT INTO enrolments VALUES (6, 'C011');
INSERT INTO enrolments VALUES (7, 'C001');
INSERT INTO enrolments VALUES (7, 'C004');
INSERT INTO enrolments VALUES (8, 'C005');
INSERT INTO enrolments VALUES (8, 'C006');
INSERT INTO enrolments VALUES (8, 'C007');
INSERT INTO enrolments VALUES (9, 'C002');
INSERT INTO enrolments VALUES (9, 'C003');
INSERT INTO enrolments VALUES (9, 'C005');
INSERT INTO enrolments VALUES (10, 'C007');
INSERT INTO enrolments VALUES (10, 'C009');
INSERT INTO enrolments VALUES (11, 'C008');
INSERT INTO enrolments VALUES (11, 'C011');