show databases;

-- Creating the Database
CREATE DATABASE ELearningPlatform;
USE ELearningPlatform;

-- Students Table
CREATE TABLE Students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    enrollment_date DATE
);

ALTER TABLE Students ADD COLUMN last_activity_time 
TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP;

UPDATE Students SET last_activity_time = CURRENT_TIMESTAMP WHERE student_id = '2';


Select * from Students;

-- Instructors Table
CREATE TABLE Instructors (
    instructor_id INT PRIMARY KEY,
    instructor_name VARCHAR(100),
    expertise_area VARCHAR(100)
);

Select * from Instructors;

-- Courses Table
CREATE TABLE Courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100),
    instructor_id INT,
    start_date DATE,
    end_date DATE,
    description TEXT,
    FOREIGN KEY (instructor_id) REFERENCES Instructors(instructor_id)
);

Select * from Courses;

-- Enrollments Table
CREATE TABLE Enrollments (
    enrollment_id INT PRIMARY KEY,
    student_id INT,
    course_id INT,
    enrollment_date DATE,
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);

Select * from Enrollments;

-- Assessments Table
CREATE TABLE Assessments (
    assessment_id INT PRIMARY KEY,
    course_id INT,
    assessment_name VARCHAR(100),
    max_score INT,
    assessment_date DATE,
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);

Select * from Assessments;

-- Certificates Table
CREATE TABLE Certificates (
    certificate_id INT PRIMARY KEY,
    student_id INT,
    course_id INT,
    issue_date DATE,
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);

Select * from Certificates;

-- Forums Table
CREATE TABLE Forums (
    forum_id INT PRIMARY KEY,
    course_id INT,
    topic VARCHAR(100),
    post_date DATETIME,
    author_id INT,
    content TEXT,
    FOREIGN KEY (course_id) REFERENCES Courses(course_id),
    FOREIGN KEY (author_id) REFERENCES Students(student_id)
);

Select * from Forums;

show tables;
