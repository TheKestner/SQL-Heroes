# This is why you'll execute a series of SQL statements during demo day.
from connection import execute_query
from create import create_hero

# gather_heroes = """
#     SELECT * FROM heroes
#     ORDER BY id 
# """

# heroes = execute_query(gather_heroes).fetchall()
# for hero in heroes:
#     print(hero[1])

# INSERT INTO
#     heroes (name, about_me, biography)
# VALUES
#     (
#         'The DoorMan',
#         'Just a Door...Literally.',
#         'Not much to say about a Door'
#     );

# def get_it():
#     gather_heroes = """
#     SELECT * FROM heroes
#     ORDER BY id
#     """
#     heroes = execute_query(gather_heroes).fetchall()
#     for hero in heroes:
#         print("Here is your current heroes:", hero[1])
# get_it()


name = input("What is your Hero name? ")
about = input("Tell us about yourself: ")
bio = input("Copy and paste your bio from the internet: ")
create_hero(name, about, bio)





# u = input("What is your Heroes ablility? ")
# print("Your ability is now", u+"!")







# d = input("Do you want to delete ALL heroes? Either y/n: ")
# print("oh no, Heroes no longer exist")

## delete all heroes sql