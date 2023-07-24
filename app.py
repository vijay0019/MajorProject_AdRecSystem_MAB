from flask import Flask, g, render_template, request, redirect, url_for
import sqlite3
import math
from math import log, sqrt
from random import betavariate, random, choice
import os

app = Flask(__name__)

# Configuration variables
DATABASE = 'ads.db'
NUM_AD_CHOICES = 3
UCB_C = 2

# dbect to the database
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

# Close the database dbection at the end of each request
@app.teardown_appcontext
def close_dbection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# Select an ad using the UCB algorithm
def select_ad():
    ads = []
    impressions = []
    clicks = []
    total_impressions = 0

    # Retrieve ad data from the database
    db = get_db()
    cursor = db.execute('SELECT * FROM ads')
    rows = cursor.fetchall()
    for row in rows:
        ads.append(row[0])
        impressions.append(row[1])
        clicks.append(row[2])
        total_impressions += row[1]

    # Use the UCB algorithm to select an ad
    ucb_values = []
    for i in range(len(ads)):
        if impressions[i] == 0:
            ucb_values.append(float('inf'))
        else:
            mean_reward = clicks[i] / impressions[i]
            bonus = UCB_C * math.sqrt(math.log(total_impressions) / impressions[i])
            ucb_values.append(mean_reward + bonus)

    ad_index = ucb_values.index(max(ucb_values))
    ad = ads[ad_index]

    return ad

# Render the homepage
@app.route('/')
def home():
    return render_template('home2.html')

# Choose an ad and render the ad template
# @app.route('/ad')
# def ad():
#     ad = select_ad()

#     # Increment the impression count for the selected ad
#     db = get_db()
#     cursor = db.cursor()
#     cursor.execute('UPDATE ads SET impressions = impressions + 1 WHERE category = ?', [ad])
#     db.commit()

    # return render_template('ad2.html', ad=ad)

@app.route('/ad_thompson_eps')
def get_ad_thompson_eps(epsilon=0.1):
    # Retrieve ad data from the database
    db = get_db()
    cursor = db.execute(f'SELECT * FROM cats')
    cats_data = cursor.fetchall()
    cats = [cat[0] for cat in cats_data]

    if not cats:
        best_cat = None
    total_impressions = sum(cat[1] for cat in cats_data)
    if total_impressions == 0 or random() < epsilon:
        best_cat = choice(cats)
        cursor2 = db.execute('SELECT name FROM ads where category = ?', [best_cat])
        ads = cursor2.fetchall()
        imgs = [ad[0] for ad in ads]
        name = choice(imgs)
        best_ad = f'{best_cat}/{name}'
    else:
        max_upper_bound = -float('inf')
        best_cat = None
        for cat in cats_data:
            category, impressions, clicks = cat
            alpha = clicks + 1
            beta = impressions - clicks + 1
            sample = betavariate(alpha, beta)
            upper_bound = sample
            if upper_bound > max_upper_bound:
                max_upper_bound = upper_bound
                best_cat = category
                cursor2 = db.execute('SELECT name FROM ads where category = ? and impressions = 0', [best_cat])
                ads = cursor2.fetchall()
                imgs = [ad[0] for ad in ads]
                name = choice(imgs)
                best_ad = f'{best_cat}/{name}'

    cursor.execute('UPDATE cats SET impressions = impressions + 1 WHERE category = ?', [best_cat])
    cursor2.execute('UPDATE ads SET impressions = impressions + 1 WHERE name = ?', [name])
    db.commit()

    return render_template('ad2.html', ad=best_ad)


@app.route('/clicked', methods=['POST'])
def click():
    # Record the ad click
    ad = request.form['ad']
    cat = ad.split('/')[0]
    
    if '.gif' not in ad:
        db = get_db()
        cursor = db.cursor()
        cursor.execute('UPDATE cats SET clicks = clicks + 1 WHERE category = ?', [cat])
        db.commit()
    
    # Redirect to the home page
    return redirect(url_for('home'))

@app.route('/stats')
def stats():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM cats")
    rows = cursor.fetchall()
    return render_template('stats2.html', rows=rows)

if __name__ == '__main__':
    app.run(debug=True)
