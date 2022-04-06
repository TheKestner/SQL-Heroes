# import sys 
# sys.path.append(".")
from connection import delete

delete_table = """
DROP TABLE test;
"""

delete(delete_table)