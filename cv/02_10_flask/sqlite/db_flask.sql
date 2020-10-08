DROP TABLE IF EXISTS dt_db;
CREATE TABLE dt_db(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	title TEXT NOT NULL,
	content TEXT NOT NULL
);