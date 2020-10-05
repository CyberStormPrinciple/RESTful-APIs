DROP TABLE IF EXISTS users;

CREATE TABLE users
(
    id SERIAL PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
);

DROP TABLE IF EXISTS items;

CREATE TABLE items
(
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  price FLOAT NOT NULL
);
