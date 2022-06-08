CREATE TABLE RATE_ANALYSIS (
	ID INT IDENTITY(1,1) PRIMARY KEY,
	MEDIA_CONTENT VARCHAR(100),
	IMPRESSIONS VARCHAR(100),
	POSITIVE INT,
	NEGATIVE INT,
	NEUTRAL INT
);

INSERT INTO RATE_ANALYSIS (MEDIA_CONTENT, IMPRESSIONS, POSITIVE, NEGATIVE, NEUTRAL) VALUES  ('Dick Johnson Is Dead', 'good', 102, 115, 204),
                                                                                            ('Blood Water', 'much', 68, 56, 189),
                                                                                            ('Ganglands', 'fine', 73, 58, 209),
                                                                                            ('Stranger Things', 'wonderful', 376, 98, 539),
                                                                                            ('Dark', 'good', 208, 117, 480),
																							('Pretty Little Liars', 'boring', 180, 187, 436),
																							('Percy Jackson', 'good', 166, 129, 453),
																							('Monsters', 'good', 124, 78, 267),
																							('Monsters', 'fine', 149, 178, 337),
                                                                                            ('Stranger Things', 'good', 490, 132, 639),
                                                                                            ('Stranger Things', 'perfect', 478, 124, 616);