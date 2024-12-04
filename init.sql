-- init.sql
CREATE TABLE example_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    department_id INT
);

CREATE TABLE department_table (
    department_id INT AUTO_INCREMENT PRIMARY KEY,
    department_name VARCHAR(255) NOT NULL
);

INSERT INTO department_table (department_name) VALUES ('개발팀');
INSERT INTO department_table (department_name) VALUES ('마케팅팀');
INSERT INTO department_table (department_name) VALUES ('인사팀');
INSERT INTO department_table (department_name) VALUES ('영업팀');

INSERT INTO example_table (name, email, age, department_id) VALUES ('박성현', 'sung hyun@example.com', 30, 1);
INSERT INTO example_table (name, email, age, department_id) VALUES ('김영훈', 'young hoon@example.com', 28, 2);
INSERT INTO example_table (name, email, age, department_id) VALUES ('이민지', 'min ji@example.com', 25, 3);
INSERT INTO example_table (name, email, age, department_id) VALUES ('최민수', 'min soo@example.com', 35, 1);
INSERT INTO example_table (name, email, age, department_id) VALUES ('정지훈', 'ji hoon@example.com', 27, 2);
INSERT INTO example_table (name, email, age, department_id) VALUES ('한예슬', 'ye seul@example.com', 29, 3);
INSERT INTO example_table (name, email, age, department_id) VALUES ('오하늘', 'ha neul@example.com', 24, 1);
INSERT INTO example_table (name, email, age, department_id) VALUES ('김수현', 'soo hyun@example.com', 32, 2);
INSERT INTO example_table (name, email, age, department_id) VALUES ('박지민', 'ji min@example.com', 26, 3);
INSERT INTO example_table (name, email, age, department_id) VALUES ('이동욱', 'dong wook@example.com', 33, 1);