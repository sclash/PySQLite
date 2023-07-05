from time import perf_counter
import pandas as pd
import sqlite3

from random import sample
from string import ascii_lowercase

db = sqlite3.connect('SQLite/names_test.db')
cur = db.cursor()


# query = f"""
# INSERT INTO {self.value.table} name
# SELECT '{new_name}'
# WHERE NOT EXISTS (
#     SELECT 1
#     FROM {self.value.table}
#     WHERE name = '{new_name}'
# )
# """

def random_string(n_char: int = 15) -> str:
    r_s = sample(list(ascii_lowercase), n_char)
    return ''.join(r_s).title()

random_names = [random_string() for i in range(1000)]


start = perf_counter()
name = pd.read_sql(sql = "SELECT * from first_name",con = db)
name_to_add = set(name['name']).union(set(random_names)) - set(name['name'])
print(f"ADDING {len(name_to_add)} names")
cur.executemany("INSERT INTO first_name (name) VALUES (?)", [(i,) for i in list(name_to_add)])
end = perf_counter()
print(f"Pandas Time: {end-start}")  #### ~.1s



start = perf_counter()
print(f"ADDING {len(name_to_add)} names")
cur.executemany("""INSERT INTO first_name (name)
                    SELECT (?)
                    WHERE NOT EXISTS (
                    SELECT 1
                    FROM first_name
                    WHERE name = (?)
                    )
                """, 
                
                [(i,i) for i in random_names])
end = perf_counter()
print(f"SQL Time: {end-start}")  ### ~4s


###### PANDAS AND SET OPERATIONS IN PYTHON ARE MUCH FASTER ######