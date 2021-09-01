import psycopg2
from psycopg2 import sql
from contextlib import closing
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import config


#conn = psycopg2.connect(dbname=config.dbname, user=config.user, password=config.password, host='127.0.0.1')
def randId():
    with psycopg2.connect(dbname=config.dbname, user=config.user, password=config.password, host='127.0.0.1') as conn:
        with conn.cursor() as cursor:
            req = sql.SQL('SELECT cfid FROM tasks WHERE rank < 1200 and rank > 1000 ORDER BY random() LIMIT 1')
            cursor.execute(req)
            otv = cursor.fetchone()[0]
            num = otv[:-1]
            let = otv[-1]
            adr = f"https://codeforces.com/problemset/problem/{num}/{let}"
            return adr
