from connection import execute_query

update_table = """
INSERT INTO test (fakehero)
VALUES('FAKEMAN');
"""

execute_query(update_table)