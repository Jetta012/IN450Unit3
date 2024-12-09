
-- Create Roles with Login Permissions
CREATE ROLE IN450a WITH LOGIN PASSWORD 'password_a';
CREATE ROLE IN450b WITH LOGIN PASSWORD 'password_b';
CREATE ROLE IN450c WITH LOGIN PASSWORD 'password_c';

-- Create Tables
CREATE TABLE IN450a (
    id SERIAL PRIMARY KEY,
    description TEXT
);

CREATE TABLE IN450b (
    id SERIAL PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    email TEXT,
    source TEXT,
    destination TEXT
);

CREATE TABLE IN450c (
    id SERIAL PRIMARY KEY,
    info TEXT
);

-- Grant Permissions to Roles
-- IN450a: Full access to all tables
GRANT CONNECT ON DATABASE my_database TO IN450a;
GRANT USAGE ON SCHEMA public TO IN450a;
GRANT SELECT ON IN450a TO IN450a;
GRANT SELECT ON IN450b TO IN450a;
GRANT SELECT ON IN450c TO IN450a;

-- IN450b: Access to IN450b table only
GRANT CONNECT ON DATABASE my_database TO IN450b;
GRANT USAGE ON SCHEMA public TO IN450b;
GRANT SELECT ON IN450b TO IN450b;

-- IN450c: Access to IN450c table only
GRANT CONNECT ON DATABASE my_database TO IN450c;
GRANT USAGE ON SCHEMA public TO IN450c;
GRANT SELECT ON IN450c TO IN450c;

-- Ensure Each Role Can Log In
ALTER ROLE IN450a LOGIN;
ALTER ROLE IN450b LOGIN;
ALTER ROLE IN450c LOGIN;
