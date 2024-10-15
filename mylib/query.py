import os
from databricks import sql
from dotenv import load_dotenv

"""Query the database"""


def query():
    """connections to Databricks database and execute a complex query
    that contains joins, aggregation, and sorting"""
    load_dotenv()
    server_h = os.getenv("sql_server_host")
    access_token = os.getenv("mydbtoken")
    http_path = os.getenv("sql_http")
    with sql.connect(
        server_hostname=server_h,
        http_path=http_path,
        access_token=access_token,
    ) as connection:
        c = connection.cursor()
        try:
            c.execute("ALTER TABLE yirang_drink ADD COLUMN beer_percentage FLOAT")
            print("Column 'beer_percentage' added to yirang_drink table.")
        except Exception as e:
            if "FIELDS_ALREADY_EXISTS" in str(e):
                print("Column 'beer_percentage' already exists in yirang_drink table.")
            else:
                raise
        c.execute(
            """
            UPDATE yirang_drink
            SET beer_percentage = 
            (beer_servings / (beer_servings + wine_servings + spirit_servings)) * 100
            WHERE (beer_servings + wine_servings + spirit_servings) > 0
        """
        )
        result = c.execute(
            """
            SELECT
                C.continent,
                SUM(D.beer_servings) AS total_beer_servings,
                AVG(D.beer_percentage) AS avg_beer_percentage
            FROM
                yirang_drink D
            JOIN
                yirang_countries C ON D.country = C.country
            GROUP BY
                C.continent
            ORDER BY
                avg_beer_percentage DESC
        """
        ).fetchall()
        c.close()
    return result


if __name__ == "__main__":
    query()
