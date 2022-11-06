import random
import uuid
import psycopg2
from psycopg2.extras import execute_batch


conn = psycopg2.connect(
    dbname='movies_database',
    user='postgres',
    password=12345,
    host='localhost',
    port=5432,
    options='-c search_path=content',
)

cur = conn.cursor()

cur.execute('SELECT id FROM film_work')
film_works_ids = []
for data in cur.fetchall():
    film_works_ids.append(data[0])

print(data)

cur.close()
conn.close()