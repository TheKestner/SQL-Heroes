# import sys 
# sys.path.append(".")
from connection import execute_query


# execute_query(create_table) WORKS WITH INPUT
def create_hero(name, about, bio):
    your_hero = """
     INSERT INTO heroes (name, about_me, biography)
     VALUES (%s, %s, %s);
     """ 
    heroes = execute_query(your_hero, (name, about, bio))
    print("Welcome,", name+"!")










# create_table = """ 
# CREATE TABLE test (
#     fake_id INT PRIMARY KEY generated always as identity,
#     fakehero VARCHAR(50) UNIQUE NOT NULL
#     );
# """

