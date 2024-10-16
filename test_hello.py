"""
Test goes here.
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
    # Step 1: Load environment variables from .env
    load_dotenv()

    # Step 2: Get the environment variables
    server_h = os.getenv("sql_server_host")
    access_token = os.getenv("mydbtoken")
    http_path = os.getenv("sql_http")

    # Step 4: Handle None values gracefully by checking the variables
    if not server_h:
        raise ValueError(
            "Environment variable 'sql_server_host' is not set or is empty."
        )
    if not access_token:
        raise ValueError("Environment variable 'mydbtoken' is not set or is empty.")
    if not http_path:
        raise ValueError("Environment variable 'sql_http' is not set or is empty.")

    # Optional: Print for debugging to verify that variables are set correctly
    print(f"Server Host: {server_h}")
    print(f"Access Token: {access_token}")
    print(f"HTTP Path: {http_path}")

    # Step 3: Proceed to establish the connection with Databricks SQL
    with sql.connect(
        server_hostname=server_h,
        http_path=http_path,
        access_token=access_token,
    ) as connection:
        # Perform your SQL operations
        print("Connection successful!")

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
