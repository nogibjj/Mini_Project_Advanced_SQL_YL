"""
Transforms and Loads data into the local SQLite3 database
Example:
,general name,count_products,ingred_FPro,avg_FPro_products,avg_distance_root,ingred_normalization_term,semantic_tree_name,semantic_tree_node
"""

import sqlite3
import csv
import os


# load the csv file and insert into a new sqlite3 database
def load(dataset="data/drinks.csv"):
    """ "Transforms and Loads data into the local SQLite3 database"""

    # prints the full working directory and path
    print(os.getcwd())
    payload = csv.reader(open(dataset, newline=""), delimiter=",")
    conn = sqlite3.connect("data/drink.db")
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS drink")
    c.execute(
        "CREATE TABLE drink (country, beer_servings, spirit_serving, wine_servings, total_litres_of_pure_alcohol)"
    )
    # insert
    c.executemany("INSERT INTO drink VALUES (?, ?, ?, ?, ?)", payload)
    conn.commit()
    conn.close()
    return "drink.db"


if __name__ == "__main__":
    load()
