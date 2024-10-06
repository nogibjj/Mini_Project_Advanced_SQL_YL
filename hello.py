"""
ETL-Query script
"""

from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import read, create, update, delete

# Extract
print("Extracting data...")
extract()

# Transform and load
print("Transforming data...")
load()

# Query
print("Querying data...")
read()
create()
update()
delete()