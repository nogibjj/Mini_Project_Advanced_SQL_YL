"""
connect to Databricks and create queries
"""

import os
from databricks import sql
from dotenv import load_dotenv
import pandas as pd


# load the csv file and insert into a new sqlite3 database
def load(dataset="data/drinks.csv", dataset2="data/countries.csv"):
    """Transforms and loads data from Databricks database from API"""
    # df = pd.read_csv(dataset, delimiter=",", skiprows=1)
    # df2 = pd.read_csv(dataset2, delimiter=",", skiprows=1)
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
        c.execute("SHOW TABLES FROM default LIKE 'yirang*'")
        # result = c.fetchall()
        c.execute(
            """
            CREATE TABLE IF NOT EXISTS yirang_drink 
            (country string,
            beer_servings int,
            spirit_servings int,
            wine_servings int,
            total_litres_of_pure_alcohol int)
        """
        )
        # # insert query
        # values_list = [tuple(row) for _, row in df.iterrows()]
        # insert_query = (
        #     f"INSERT INTO yl1041_drink VALUES {','.join(str(x) for x in values_list)}"
        # )
        # c.execute(insert_query)

        c.execute(
            """
            CREATE TABLE IF NOT EXISTS yirang_countries 
            (continent string,
            country string)
        """
        )

        c.close()

    return "Load Success"


if __name__ == "__main__":
    load()
