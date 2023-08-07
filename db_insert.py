import sqlite3
import os


# Rename all image files
base_dir = "static/img/categories"
for cat in os.listdir(base_dir):
    for index, file_name in enumerate(os.listdir(f"{base_dir}/{cat}")):
        os.rename(f"{base_dir}/{cat}/{file_name}", f"{base_dir}/{cat}/{cat}_{index}.jpg")


# Open a connection to the database
conn = sqlite3.connect('ads.db')

# Create a cursor object to execute SQL commands
cur = conn.cursor()

# Delete all data from tables
cur.execute("DELETE from ads")
cur.execute("DELETE from cats")

# Insert some sample data into the ads table
stmt = """INSERT INTO cats (category, impressions, clicks) VALUES {}"""
values = [str((cat, 0, 0)) for cat in os.listdir('static/img/categories')]

stmt2 = """INSERT INTO ads (category, name, impressions) VALUES {}"""
values2 = [str((cat, name, 0)) for cat in os.listdir('static/img/categories') for name in os.listdir(f'static/img/categories/{cat}')]

cur.execute(stmt.format(",".join(values)))
cur.execute(stmt2.format(",".join(values2)))

# cur.execute("INSERT INTO ads (category, impressions, clicks) VALUES ('decor', 0, 0)")

# Commit the changes to the database
conn.commit()

# Close the cursor and the database connection
cur.close()
conn.close()