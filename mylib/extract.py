"""
Extract a dataset from 538
"""

import os
import requests


def extract(
    url="https://raw.githubusercontent.com/fivethirtyeight/data/e6bbbb2d35310b5c63c2995a0d03d582d0c7b2e6/alcohol-consumption/drinks.csv",
    file_path="data/drinks.csv",
    directory="data",
):
    """Extract a url to a file path"""
    if not os.path.exists(directory):
        os.makedirs(directory)
    with requests.get(url) as r:
        with open(file_path, "wb") as f:
            f.write(r.content)
    return file_path
