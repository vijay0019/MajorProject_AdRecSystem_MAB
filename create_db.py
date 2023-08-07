import sqlite3

DB_NAME = 'ads.db'

# Create the database and tables
def create_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Create category table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cats (
        category TEXT NOT NULL,
        impressions INTEGER NOT NULL,
        clicks INTEGER NOT NULL
        );
    ''')

    # Create ads table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ads (
        category TEXT NOT NULL,
        name TEXT PRIMARY KEY,
        impressions INTEGER NOT NULL
        );
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database()
    print('Database created successfully.')
