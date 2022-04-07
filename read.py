from connection import execute_query


def get_it():
    gather_heroes = """
    SELECT * FROM heroes
    ORDER BY id
    """
    heroes = execute_query(gather_heroes).fetchall()
    for hero in heroes:
        print("Here is the current heroes:", hero[1])










# join_heroes = """
#     SELECT heroes.name, relationship_types.name
#     FROM heroes
#     JOIN relationships
#     ON heroes.id = relationships.hero1_id
#     JOIN relationship_types
#     ON relationships.relationship_type_id = relationship_types.id
# """

# for hero in heroes:
#     print(hero[1])

# SELECT heroes.name, relationships.hero2_id, relationship_types.name
# FROM heroes
# JOIN relationships
# ON heroes.id = relationships.hero1_id
# JOIN relationship_types
# ON relationship_types.id = relationships.relationship_type_id