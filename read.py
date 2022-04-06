from connection import select_all

select_heroes = """
    SELECT * FROM heroes
    ORDER BY id DESC 
"""

heroes = select_all(select_heroes)
for hero in heroes:
    print(hero[1])