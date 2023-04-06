import psycopg2


#import psycopg2.extras; psycopg2.extensions.set_wait_callback(psycopg2.extras.wait_select)

# You can set the password to None if it is specified in a ~/.pgpass file
USERNAME = "crispin.carlos"
PASSWORD = "9dFUIXwRn5ut"
HOST = "pg.neon.tech"
PORT = "5432"
PROJECT = "neondb"

conn = psycopg2.connect(
 host=HOST,
 port=PORT,
 user=USERNAME,
 password=PASSWORD,
 database=PROJECT)

with conn.cursor() as cur:
    cur.execute("SELECT 'hello neon';")
    print(cur.fetchall())