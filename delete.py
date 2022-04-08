# import sys 
# sys.path.append(".")
from connection import execute_query


# delete only 1 hero 
def hero_delete(delete):
    hero_delete = """
    DELETE FROM heroes
    WHERE name = (%s)
    """
    execute_query(hero_delete, (delete,))



# may be a way to delete all tables at once
def danger_zone():
    danger_zone = """ 
    SELECT
     'DROP TABLE IF EXISTS "' || tablename || '" CASCADE;' 
    FROM
      pg_tables WHERE schemaname = 'public'; """
    execute_query(danger_zone)






# def danger_zone():
#     delete_table = """
#     DROP TABLE test;
#     """
#     execute_query(delete_table)
#danger_zone()

# gotta_delete = """
# DELETE FROM heroes
# WHERE id = 1; """
# execute_query(gotta_delete)