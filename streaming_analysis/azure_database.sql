CREATE TABLE RATE_ANALYSIS (
	ID INT IDENTITY(1,1) PRIMARY KEY,
	SHOW VARCHAR(100),
	IMPRESSIONS VARCHAR(40),
	POSITIVE VARCHAR(100),
	NEGATIVE VARCHAR(100),
	NEUTRAL VARCHAR(100)
);