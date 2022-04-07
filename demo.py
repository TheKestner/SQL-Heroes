# This is why you'll execute a series of SQL statements during demo day.
from connection import execute_query
from create import create_hero
from read import get_it



get_it()

name = input("What is your Hero name? ")
about = input("Tell us about yourself: ")
bio = input("Copy and paste your bio from the internet: ")
create_hero(name, about, bio)






# uname = input("You call that a SuperHero name? Wanna update it? ")
# uabout = input("While your at it... Wanna update the about? ")
# ubio = input("")


# delete = input("Do you want to enter the Danger Zone?" ) 
# d = input("Do you want to delete ALL heroes? Either y/n: ")
# print("oh no, Heroes no longer exist")

## delete all heroes sql