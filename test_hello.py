"""
Test goes here
"""

import os
from databricks import sql
from dotenv import load_dotenv
from mylib.extract import extract
from mylib.query import query


def test_extract():
    result = extract()
    assert result is not None, "Failed to extract the database"


def test_load():
    load_dotenv()  # Load environment variables from .env
    server_h = os.getenv("sql_server_host")
    access_token = os.getenv("mydbtoken")
    http_path = os.getenv("sql_http")

    # Debugging: Check if variables are loaded correctly
    print(f"Server Host: {server_h}")
    print(f"Access Token: {access_token}")
    print(f"HTTP Path: {http_path}")

    if not server_h or not access_token or not http_path:
        raise ValueError(
            "Environment variables for Databricks connection are not set properly."
        )

    # Proceed to establish the connection
    with sql.connect(
        server_hostname=server_h,
        http_path=http_path,
        access_token=access_token,
    ) as connection:
        # def test_load():
        #     load_dotenv()
        #     server_h = os.getenv("sql_server_host")
        #     access_token = os.getenv("mydbtoken")
        #     http_path = os.getenv("sql_http")
        #     with sql.connect(
        #         server_hostname=server_h,
        #         http_path=http_path,
        #         access_token=access_token,
        #     ) as connection:
        c = connection.cursor()
        c.execute("SHOW TABLES FROM default LIKE 'yirang*'")
        result1 = c.fetchall()
        c.execute("SELECT * FROM yirang_drink")
        result2 = c.fetchall()
        c.execute("SHOW TABLES FROM default LIKE 'yirang*'")
        result3 = c.fetchall()
        c.execute("SELECT * FROM yirang_countries")
        result4 = c.fetchall()
        c.close()
    assert result1 is not None
    assert result2 is not None
    assert result3 is not None
    assert result4 is not None


def test_query():
    result = query()
    assert result is not None, "Failed to query the database"


if __name__ == "__main__":
    test_extract()
    test_load()
    test_query()
