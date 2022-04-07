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
-- # delete(delete_table)




-- ##Joining heroes to ability numbers
--  SELECT abilities.id AS ability_number, hero_id AS ability_num, heroes.name, heroes.id AS hero_id
--  FROM abilities
--  INNER JOIN heroes ON heroes.id=abilities.hero_id;

-- ##expanding and joinging heroes to ability names
--  SELECT heroes.name, heroes.id, abilities.hero_id, abilities.ability_type_id, ability_types.name, ability_types.id
--  FROM heroes
--  FULL OUTER JOIN abilities
--  ON heroes.id = abilities.hero_id
--  FULL OUTER JOIN ability_types
--  ON abilities.ability_type_id = ability_types.id

-- ##cleaning up the result table and formatting it nicely
--  SELECT heroes.name AS Hero, ability_types.name AS Ability
--  FROM heroes
--  JOIN abilities
--  ON heroes.id = abilities.hero_id
--  JOIN ability_types
--  ON abilities.ability_type_id = ability_types.id

-- WHERE ability_types.name= 'Telepathy'
-- Tacking that on at the end makes it so you can return only the hero with that ability.



-- ## how to join tables that reference multiple foreign keys for a same table

-- SELECT heroes.name as Hero1, relationship_types.name as Relationship, h2.name as Hero2
-- FROM heroes
-- JOIN relationships
-- ON heroes.id = relationships.hero1_id
-- JOIN relationship_types
-- ON relationship_types.id = relationships.relationship_type_id
-- JOIN heroes h2 
-- ON h2.id = relationships.hero2_id

