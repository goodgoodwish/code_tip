import psycopg2  # import PostgreSQL database interface library.
import traceback

import sys
# Add PYTHONPATH, then we may import all the objects below this folder.
sys.path.insert(0, "/Users/charliezhu/git/bi-cloud/etl")

# import tool to parse .ini configuration file.
# See below link for the explaination and examples:
# http://www.postgresqltutorial.com/postgresql-python/connect/
# ConfigParser().read(), returns a 2 dimensional array, e.g.: [[a1,a2],[b1,b2], ...].
from etl.pipeline_core.config import Config
import io


class DbTool(object):
    """
    Todo: wrap init connection in a function,
    """
    # initialize a local field(object property/attribute). Constructor.
    # config = Config.load("/Users/abc/aws/database.ini")
    def __init__(self, ini_file):  # put config constructor/initializer here?
        self.config = Config.load(ini_file)

    # Build a dictionary object to connect to a database.
    # {'user': 'scala_user', 'password': '', 'host': 'localhost', 'database': 'scala_db'}
    def db_config(self, db_name):
        db = {}
        params = self.config.settings.items(db_name)
        for param in params:
            db[param[0]] = param[1]
        # print("\n", db)
        return db

    def app_name_db_passwd(self):
        return self.config.get('app_name_db', 'password')

    def psql_copy(self, file, table, db_name='local_db'):
        """
        run psql \copy command, import
        """
        try:
            app_name_db = self.db_config(db_name)
            with psycopg2.connect(**app_name_db) as conn:
                with conn.cursor() as cur:
                    # cur.copy_from(file, table, sep=",", null="")
                    sql = f"COPY {table} FROM STDIN WITH CSV HEADER"
                    cur.copy_expert(sql, file)
                    cur.execute(f"select * from {table} limit 2")
                    data = cur.fetchall()
                    print(data)
        except Exception:
            traceback.print_exc()
            print("Error on database operation.")

    def psql_copy_raw(self, file, sql, table, db_name='local_db'):
        """
        run psql \copy command, import
        """
        try:
            app_name_db = self.db_config(db_name)
            with psycopg2.connect(**app_name_db) as conn:
                with conn.cursor() as cur:
                    # cur.copy_from(file, table, sep=",", null="")
                    cur.copy_expert(sql, file)
                    cur.execute(f"select * from {table} limit 2")
                    data = cur.fetchall()
                    print(data)
        except Exception:
            traceback.print_exc()
            print("Error on database operation.")

    def psql_export(self, file, query, db_name='local_db'):
        """
        run psql \copy command, export
        """
        try:
            app_name_db = self.db_config(db_name)
            with psycopg2.connect(**app_name_db) as conn:
                with conn.cursor() as cur:
                    # cur.copy_from(file, table, sep=",", null="")
                    sql = f"COPY {query} TO STDOUT WITH CSV HEADER"
                    cur.copy_expert(sql, file)
        except Exception:
            traceback.print_exc()
            print("Error on database operation.")

    def run_sql(self, sql, db_name='local_db'):
        """
        run sql command
        """
        try:
            app_name_db = self.db_config(db_name)
            with psycopg2.connect(**app_name_db) as conn:
                with conn.cursor() as cur:
                    cur.execute(sql)
        except Exception:
            traceback.print_exc()
            print(f"can not run {sql} ")

def test_query(conn, app_name_db_passwd):
    # Use loan pattern to open a cursor, it'll be automatically closed after exit the scope.
    with conn.cursor() as cur:
        cur.execute("""SELECT table_catalog, table_schema, table_name
      FROM information_schema.tables LIMIT 4
    """)
        rows = cur.fetchall()
        print("\nShow me the data:\n")
        for row in rows:
            print("output:   ", row[0], row[2])

def psql_copy_demo(cur):
    """
    drop table test
    create table test(
        id integer,
        name text
    );
    """
    # with io.StringIO("42\tfoo\n74\tbar\n") as f:
    with open("/Users/charliezhu/work/bi/python/t.txt") as f1:
        output = ""
        for line in [line for line in f1 if '4' in line]:
            output += line
        f = io.StringIO(output)
        cur.copy_from(f, 'test', sep=",", columns=('id', 'name'), null="")
        cur.execute("select * from test where id > 5;")
        data = cur.fetchall()
        print(data)

def main():
    try:
        app_name_tool = DbTool(
            "/Users/charliezhu/app/box/aws/database.ini")
        app_name_db = app_name_tool.db_config(db_name='local_db')
        # Same loan pattern, but for database connection.
        # **app_name_db, unpack dictionary to key value pairs arguments lists.
        # see, https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists
        with psycopg2.connect(**app_name_db) as conn:
            test_query(conn, app_name_tool.app_name_db_passwd())
            with conn.cursor() as cur:
                psql_copy_demo(cur)
    except KeyError:
        traceback.print_exc()
        print("key not found ==== ====")
    except Exception:
        traceback.print_exc()
        print("I am unable to connect to the database")


#  if run as the single script, run main method.
if __name__ == '__main__':
    main()
