# Ad Recommendation System using Multi-Armed Bandit Algorithm

## Introduction

This project is a web-based ad recommendation system that utilizes the multi-armed bandit algorithm to optimize the display of ads to the user. The system aims to improve the efficiency and effectiveness of online advertising by dynamically selecting and displaying ads based on user interactions and the exploration-exploitation trade-off.

## Features

- Recommends ads to a user based on the historical interactions and the multi-armed bandit algorithm.
- Balances between exploring new ads and exploiting the best-performing ads.
- Records user clicks and interactions to improve recommendations over time.
- Provides a user-friendly frontend interface to display recommended ads.
- Utilizes a SQLite database to store ad and interaction data.

## Installation

1. Clone the repository: `git clone https://github.com/vijay0019/MajorProject_AdRecSystem_MAB.git`
2. Navigate to the project directory: `cd MajorProject_AdRecSystem_MAB`
3. Install required packages: `pip install -r requirements.txt`
4. Create and set up the SQLite database: `python create_db.py`
5. Create a directory `static/img/categories` and then create 5 additional directories with the category name and add some images in each of them:
    - `static/img/clothes`
    - `static/img/decor`
    - `static/img/food`
    - `static/img/footwear`
    - `static/img/wellness`
6. Insert data into the tables: `python db_insert.py`
7. Run the Flask web application: `python app.py`

## Usage

1. Access the frontend by opening a web browser and navigating to `http://localhost:5000`.
2. Users can view recommended ads on the homepage.
3. Users can click on an ad to record their interaction.
4. The system will update the recommendations based on user interactions and the multi-armed bandit algorithm.

## Acknowledgements

- This project is inspired by the concept of multi-armed bandits and their application in recommendation systems.
- Thanks to the Flask and SQLite communities for providing helpful resources and documentation.