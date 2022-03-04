CREATE DATABASE test_script;
USE test_script;

CREATE TABLE datas (
    id INT PRIMARY KEY AUTO_INCREMENT,
    tempo_execucao VARCHAR(25),
    espaco_alocado VARCHAR(25),
    quantidade_iteracoes VARCHAR(25),
    script VARCHAR(25)
);