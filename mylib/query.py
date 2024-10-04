"""Query the database"""

import sqlite3

# Define a global variable for the log file
LOG_FILE = "query_log.md"


def log_query(query):
    """adds to a query markdown file"""
    with open(LOG_FILE, "a") as file:
        file.write(f"```sql\n{query}\n```\n\n")


def general_query(query):
    """runs a query a user inputs"""
    # Connect to the SQLite database
    conn = sqlite3.connect("drink.db")

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Execute the query
    cursor.execute(query)

    # If the query modifies the database, commit the changes
    if (
        query.strip().lower().startswith("insert")
        or query.strip().lower().startswith("update")
        or query.strip().lower().startswith("delete")
    ):
        conn.commit()

    # Close the cursor and connection
    cursor.close()
    conn.close()

    log_query(f"{query}")


def create_record(
    country, beer_servings, spirit_servings, wine_servings, total_litres_of_pure_alcohol
):
    """create example query"""
    conn = sqlite3.connect("drink.db")
    c = conn.cursor()
    c.execute(
        """
        INSERT INTO drink 
        (country, beer_servings, spirit_servings, wine_servings, total_litres_of_pure_alcohol) 
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            country,
            beer_servings,
            spirit_servings,
            wine_servings,
            total_litres_of_pure_alcohol,
        ),
    )
    conn.commit()
    conn.close()

    # Log the query
    log_query(
        f"""INSERT INTO ServeTimesDB VALUES (
            {country}, 
            {beer_servings}, 
            {spirit_servings}, 
            {wine_servings}, 
            {total_litres_of_pure_alcohol});"""
    )


def update_record(
    record_id,
    country,
    beer_servings,
    spirit_servings,
    wine_servings,
    total_litres_of_pure_alcohol,
):
    """update example query"""
    conn = sqlite3.connect("drink.db")
    c = conn.cursor()
    c.execute(
        """
        UPDATE drink 
        SET country=?, 
        beer_servings=?, 
        spirit_servings=?, 
        wine_servings=?, 
        total_litres_of_pure_alcohol=?,
        WHERE id=?
        """,
        (
            country,
            beer_servings,
            spirit_servings,
            wine_servings,
            total_litres_of_pure_alcohol,
            record_id,
        ),
    )
    conn.commit()
    conn.close()

    # Log the query
    log_query(
        f"""UPDATE drink SET 
        country={country}, 
        beer_servings=
        {beer_servings},
        spirit_servings={spirit_servings}, wine_servings={wine_servings}, 
        total_litres_of_pure_alcohol={total_litres_of_pure_alcohol},
        WHERE id={record_id};"""
    )


def delete_record(record_id):
    """delete example query"""
    conn = sqlite3.connect("drink.db")
    c = conn.cursor()
    c.execute("DELETE FROM drink WHERE country=?", (record_id))
    conn.commit()
    conn.close()

    # Log the query
    log_query(f"DELETE FROM drink WHERE country={record_id};")


def read_data():
    """read data"""
    conn = sqlite3.connect("drink.db")
    c = conn.cursor()
    c.execute("SELECT * FROM drink")
    data = c.fetchall()
    log_query("SELECT * FROM drink;")
    return data


if __name__ == "__main__":
    # log_query()
    # general_query()
    # create_record()
    # update_record()
    # delete_record()
    # read_data()
