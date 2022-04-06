# import sys 
# sys.path.append(".")
from connection import execute_query

create_table = """ 
CREATE TABLE test (
    fake_id INT PRIMARY KEY generated always as identity,
    fakehero VARCHAR(50) UNIQUE NOT NULL
    );
"""

execute_query(create_table)