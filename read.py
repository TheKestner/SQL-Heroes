from connection import execute_query


def get_it():
    gather_heroes = """
    SELECT * FROM heroes
    ORDER BY id
    """
    heroes = execute_query(gather_heroes).fetchall()
    for hero in heroes:
        print("Here is the current heroes:", hero[1])


def what_is():
    baby_dont_hurt_me = """
    SELECT heroes.name as Hero1, relationship_types.name as Relationship, h2.name as Hero2
    FROM heroes
    JOIN relationships
    ON heroes.id = relationships.hero1_id
    JOIN relationship_types
    ON relationship_types.id = relationships.relationship_type_id
    JOIN heroes h2 
    ON h2.id = relationships.hero2_id
    """
    heroes = execute_query(baby_dont_hurt_me).fetchall()
    for hero in heroes:
        print("Heroes 1:",hero[0], "|| Relationship Status:",hero[1], "|| Hero 2:",  hero[2])














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