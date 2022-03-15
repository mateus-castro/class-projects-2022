CREATE DATABASE test_script;
USE test_script;

CREATE TABLE datas (
    id INT PRIMARY KEY AUTO_INCREMENT,
    execution_time VARCHAR(25),
    allocation_size VARCHAR(25),
    iterations_quantity VARCHAR(25),
    script VARCHAR(25),
    range_limit VARCHAR(10),
    step VARCHAR(10),
    created_time VARCHAR(30)
);