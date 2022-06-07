CREATE DATABASE streaming;
USE streaming;

-- criando tabela de tweets
CREATE TABLE SOCIAL_MEDIA (
	ID INT AUTO_INCREMENT PRIMARY KEY,
	USER_MESSAGE VARCHAR(140),
	USER_NICK VARCHAR(40),
	POSITIVE JSON,
	NEGATIVE JSON,
	NEUTRAL JSON
);

-- criando tabela de títulos disponíveis para streaming na plataforma
CREATE TABLE CONTENT (
	ID INT AUTO_INCREMENT PRIMARY KEY,
	CATEGORY VARCHAR(20) NOT NULL,
	TITLE VARCHAR(50) NOT NULL,
	DIRECTORS JSON,
	CAST_MEMBERS JSON,
	COUNTRY VARCHAR(50),
	DATE_ADDED DATE,
	RELEASE_YEAR YEAR NOT NULL,
	RATING VARCHAR(20),
	DURATION VARCHAR(30),
	LISTED_IN JSON NOT NULL,
	SHOW_DESC VARCHAR(50)
);