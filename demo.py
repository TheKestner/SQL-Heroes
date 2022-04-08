from connection import execute_query
from create import create_hero
from read import get_it, what_is
from delete import hero_delete, danger_zone

# lets get it superheroes

get_it()


# lets you create your superhero via terminal input

name = input("What is your Hero name? ")
about = input("Tell us about yourself: ")
bio = input("Copy and paste your bio from the internet: ")
create_hero(name, about, bio)



# lets you find relationships between heroes
def what_is_love():
    status = input("Do you want to find love? Yes or No: ")
    find = status.lower()
    if find == 'yes':
        what_is()
    elif find == 'no':
        print('No Love')        
what_is_love()

#destroy hero
def destroy_hero():
    delete = input("Do you want to destory a hero? Enter name or no: ")
    if delete == 'no':
        print('Good Job! You are acting like a real hero.')
    else:
        hero_delete(delete)
        print("Wow, you actually did it..")
destroy_hero()


# Attempt a delete all 
def drop_like_its_hot():
    delete = input("Do you want to be worse than Thanos? Yes or No: ")
    find = status.lower()
    if find == 'yes':
        danger_zone()
        print('Good Bye World')
    elif find == 'no':
        print('Good Job! The World is still safe.')
# drop_like_its_hot()








# uname = input("You call that a SuperHero name? Wanna update it? ")
# uabout = input("While your at it... Wanna update the about? ")
# ubio = input("")


# delete = input("Do you want to enter the Danger Zone?" ) 
# d = input("Do you want to delete ALL heroes? Either y/n: ")
# print("oh no, Heroes no longer exist")

## delete all heroes sql