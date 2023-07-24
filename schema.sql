CREATE TABLE IF NOT EXISTS cats (
    category TEXT NOT NULL,
    impressions INTEGER NOT NULL,
    clicks INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS ads (
    category TEXT NOT NULL,
    name TEXT PRIMARY KEY,
    impressions INTEGER NOT NULL
);