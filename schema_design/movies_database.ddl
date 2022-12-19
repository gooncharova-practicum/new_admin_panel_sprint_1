CREATE SCHEMA IF NOT EXISTS content;

CREATE TABLE IF NOT EXISTS content.film_work (
    id uuid PRIMARY KEY, 
    title TEXT NOT NULL,
    description TEXT, 
    creation_date DATE, 
    rating FLOAT, 
    type TEXT CHECK (type IN ('tv_show', 'movie')) NOT NULL, 
    created timestamp with time zone, 
    modified timestamp with time zone
);

CREATE TABLE IF NOT EXISTS content.genre (
    id uuid PRIMARY KEY, 
    name TEXT NOT NULL UNIQUE, 
    description TEXT, 
    created timestamp with time zone, 
    modified timestamp with time zone
);

CREATE TABLE IF NOT EXISTS content.genre_film_work (
    id uuid PRIMARY KEY, 
    genre_id uuid NOT NULL REFERENCES genre ON DELETE CASCADE, 
    film_work_id uuid NOT NULL REFERENCES film_work ON DELETE CASCADE, 
    created timestamp with time zone
);

CREATE TABLE IF NOT EXISTS content.person (
    id uuid PRIMARY KEY, 
    full_name TEXT NOT NULL, 
    created timestamp with time zone, 
    modified timestamp with time zone
);

CREATE TABLE IF NOT EXISTS content.person_film_work (
    id uuid PRIMARY KEY, 
    person_id uuid NOT NULL REFERENCES person ON DELETE CASCADE, 
    film_work_id uuid NOT NULL REFERENCES film_work ON DELETE CASCADE, 
    role TEXT NOT NULL, 
    created timestamp with time zone
);

CREATE INDEX IF NOT EXISTS film_work_creation_date_idx ON content.film_work(creation_date); 
CREATE INDEX IF NOT EXISTS person_full_name_idx ON content.person(full_name);
CREATE INDEX IF NOT EXISTS genre_name_idx ON content.genre(name);