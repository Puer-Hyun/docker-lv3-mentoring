-- init.sql
CREATE TABLE example_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    age INT NOT NULL
);

INSERT INTO example_table (name, email, age) VALUES ('박성현', 'sung hyun@example.com', 30);
INSERT INTO example_table (name, email, age) VALUES ('김영훈', 'young hoon@example.com', 28);
INSERT INTO example_table (name, email, age) VALUES ('이민지', 'min ji@example.com', 25);
INSERT INTO example_table (name, email, age) VALUES ('최민수', 'min soo@example.com', 35);
INSERT INTO example_table (name, email, age) VALUES ('정지훈', 'ji hoon@example.com', 27);
INSERT INTO example_table (name, email, age) VALUES ('한예슬', 'ye seul@example.com', 29);
INSERT INTO example_table (name, email, age) VALUES ('오하늘', 'ha neul@example.com', 24);
INSERT INTO example_table (name, email, age) VALUES ('김수현', 'soo hyun@example.com', 32);
INSERT INTO example_table (name, email, age) VALUES ('박지민', 'ji min@example.com', 26);
INSERT INTO example_table (name, email, age) VALUES ('이동욱', 'dong wook@example.com', 33);
