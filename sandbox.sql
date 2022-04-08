-- # create_table = """ 
-- # CREATE TABLE test (
-- #     fake_id INT PRIMARY KEY generated always as identity,
-- #     fakehero VARCHAR(50) UNIQUE NOT NULL
-- #     );
-- # """

-- # execute_query(create_table)

-- # delete_table = """
-- # DROP TABLE test;
-- # """
-- # execute_query(delete_table)

-- # def get_it():
-- #     gather_heroes = """
-- #     SELECT * FROM heroes
-- #     ORDER BY id
-- #     """
-- #     heroes = execute_query(gather_heroes).fetchall()
-- #     for hero in heroes:
-- #         print("Here is your current heroes:", hero[1])






-- ## how to join tables that reference multiple foreign keys for a same table

-- SELECT heroes.name as Hero1, relationship_types.name as Relationship, h2.name as Hero2
-- FROM heroes
-- JOIN relationships
-- ON heroes.id = relationships.hero1_id
-- JOIN relationship_types
-- ON relationship_types.id = relationships.relationship_type_id
-- JOIN heroes h2 
-- ON h2.id = relationships.hero2_id




-- def update_hero(name,):
--     changed_hero = """
--     UPDATE heroes
--     SET name
--     WHERE name = %s;
--     """
--     heroes = execute_query(changed_hero, ())

