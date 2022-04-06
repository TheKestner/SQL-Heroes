# This is why you'll execute a series of SQL statements during demo day.
from connection import execute_query, delete

# select_heroes = """
#     SELECT * FROM heroes
#     ORDER BY id DESC 
# """

# heroes = execute_query(select_heroes).fetchall()
# for hero in heroes:
#     print(hero[1])

# create_table = """ 
# CREATE TABLE test (
#     fake_id INT PRIMARY KEY generated always as identity,
#     fakehero VARCHAR(50) UNIQUE NOT NULL
#     );
# """

# execute_query(create_table)

# delete_table = """
# DROP TABLE test;
# """
# delete(delete_table)