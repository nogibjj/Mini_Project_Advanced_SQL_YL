"""Query the database"""

import sqlite3


def read():
    """Read and print the database for all the rows of the drink table"""
    conn = sqlite3.connect("data/drink.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM drink")
    print(cursor.fetchall())
    conn.close()
    return "Successfully read!"


def create():
    """Create a fake data"""
    conn = sqlite3.connect("data/drink.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO drink VALUES ('Kong Hong SAR','10','10','10','10')")
    conn.commit()
    conn.close()
    return "Sucessfully created!"


def update():
    """Update China's beer_servings to be 80"""
    conn = sqlite3.connect("data/drink.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE drink SET beer_servings = '80' WHERE country = 'China';")
    conn.commit()
    conn.close()
    return "Successfully updated!"


def delete():
    """Delete rows that year is equal to 2000"""
    conn = sqlite3.connect("data/drink.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM drink WHERE country = 'North Korea';")
    conn.commit()
    conn.close()
    return "Sucessfully deleted!"


if __name__ == "__main__":
    read()
    create()
    update()
    delete()
