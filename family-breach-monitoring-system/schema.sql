-- Database schema for family profiles and breach history
CREATE TABLE family_members (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT UNIQUE
);

CREATE TABLE breaches (
    id INTEGER PRIMARY KEY,
    member_id INTEGER,
    breach_name TEXT,
    date_found DATE
);