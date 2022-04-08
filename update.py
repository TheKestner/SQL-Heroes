from connection import execute_query



def update_hero():
    changed_hero = """
    UPDATE heroes
    SET name = 'Mandoor'
    WHERE name = 'Doorman'
    """
    execute_query(changed_hero)
update_hero()












# def update_hero():
#     changed_hero = """
#     UPDATE test
#     SET fakehero = 'MANFAKE'
#     WHERE fakehero = 'FAKEMAN'
# """
#     execute_query(changed_hero)
# update_hero()


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