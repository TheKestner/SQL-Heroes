from connection import execute_query

# update_table = """
# INSERT INTO test (fakehero)
# VALUES('FAKEMAN');
# """

# execute_query(update_table)

# update_heroes = """
# INSERT INTO
#     heroes (name, about_me, biography)
# VALUES ( 'Doorman', 'I CAN MAKE DOORS', 'Doorman is a guy who can use his body to make a door... hence the name.' );
# """

# execute_query(update_heroes)


# def create_hero(name, about, bio):
#     your_hero = """
#      INSERT INTO heroes (name, about_me, biography)
#      VALUES (%s, %s, %s);
#      """ 
#     heroes = execute_query(your_hero, (name, about, bio))
#     print("Welcome,", name+"!")

# def update_hero(name,):
#     changed_hero = """
#     UPDATE heroes
#     SET name
#     WHERE name = %s;
#     """
#     heroes = execute_query(changed_hero, ())


# def update_hero():
#     changed_hero = """
#     UPDATE heroes
#     SET name
#     WHERE name = %s;
#     """
#     heroes = execute_query(changed_hero)