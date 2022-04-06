##Joining heroes to ability numbers
# SELECT abilities.id AS ability_number, hero_id AS ability_num, heroes.name, heroes.id AS hero_id
# FROM abilities
# INNER JOIN heroes ON heroes.id=abilities.hero_id;

##expanding and joinging heroes to ability names
# SELECT heroes.name, heroes.id, abilities.hero_id, abilities.ability_type_id, ability_types.name, ability_types.id
# FROM heroes
# FULL OUTER JOIN abilities
# ON heroes.id = abilities.hero_id
# FULL OUTER JOIN ability_types
# ON abilities.ability_type_id = ability_types.id

##cleaning up the result table and formatting it nicely
# SELECT heroes.name AS Hero, ability_types.name AS Ability
# FROM heroes
# JOIN abilities
# ON heroes.id = abilities.hero_id
# JOIN ability_types
# ON abilities.ability_type_id = ability_types.id

WHERE ability_types.name= 'Telepathy'

Tacking that on at the end makes it so you can return only the hero with that ability.


-- SELECT heroes.name, relationship_types.name
-- FROM heroes
-- JOIN relationships
-- ON heroes.id = relationships.hero1_id 
-- JOIN relationship_types
-- ON relationships.relationship_type_id = relationship_types.id 
-- failed attempt to show both relationships joined together 

-- SELECT heroes.name, relationship_types.name
-- FROM relationships
-- JOIN heroes
-- ON relationships.hero1_id  = heroes.id or relationships.hero2_id = heroes.id
-- JOIN relationship_types
-- ON relationships.relationship_type_id = relationship_types.id 

