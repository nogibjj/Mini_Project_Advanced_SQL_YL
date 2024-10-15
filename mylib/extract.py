"""
Extract a dataset from 538
"""

import os
import requests


def extract(
    url="https://raw.githubusercontent.com/fivethirtyeight/data/e6bbbb2d35310b5c63c2995a0d03d582d0c7b2e6/alcohol-consumption/drinks.csv",
    url2="https://raw.githubusercontent.com/dbouquin/IS_608/refs/heads/master/NanosatDB_munging/Countries-Continents.csv",
    file_path="data/drinks.csv",
    file_path2="data/countries.csv",
    directory="data",
):
    """Extract urls to a file path"""
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    def download_file(url, file_path):
        response = requests.get(url)
        if response.status_code == 200:
            with open(file_path, "wb") as f:
                f.write(response.content)
            print(f"File successfully downloaded to {file_path}")
        else:
            print(
                f"Failed to retrieve the file from {url}."
                f"Status Code: {response.status_code}"
            )

    download_file(url, file_path)
    download_file(url2, file_path2)

    return file_path, file_path2


if __name__ == "__main__":
    extract()
