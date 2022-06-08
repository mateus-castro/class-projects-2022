CREATE TABLE RATE_ANALYSIS (
	ID INT IDENTITY(1,1) PRIMARY KEY,
	MEDIA_CONTENT VARCHAR(100),
	IMPRESSIONS VARCHAR(100),
	POSITIVE INT,
	NEGATIVE INT,
	NEUTRAL INT
);

INSERT INTO RATE_ANALYSIS (MEDIA_CONTENT, IMPRESSIONS, POSITIVE, NEGATIVE, NEUTRAL) VALUES  ('Dick Johnson Is Dead', 'good, bad, awful, nice, pretty', 102, 115, 204),
                                                                                            ('Blood & Water', 'much, good, gross, nice, wow', 102, 115, 204);
