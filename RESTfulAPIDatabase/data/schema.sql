DROP TABLE IF EXISTS users;

CREATE TABLE users
(
    id INTEGER PRIMARY KEY,
    username Text NOT NULL,
    email Text NOT NULL UNIQUE,
    password Text NOT NULL
);
