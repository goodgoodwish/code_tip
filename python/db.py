import psycopg2 # import PostgreSQL database interface library.
import traceback

import sys
# Add PYTHONPATH, then we may import all the objects below this folder.
sys.path.insert(0,"/Users/abc/git/cloud/etl")  

# import tool to parse .ini configuration file.
# See below link for the explaination and examples:
# http://www.postgresqltutorial.com/postgresql-python/connect/
# ConfigParser().read(), returns 2 dimensional array, e.g.: [[a1,a2],[b1,b2], ...].
from etl.pipeline_core.config import Config

class DbTool(object):
  # initialize a local field(object property/attribute). Constructor.
  # config = Config.load("/Users/abc/aws/database.ini")
  def __init__(self, ini_file) # put config constructor/initializer here?
    config = Config.load(ini_file)

  # Build a dictionary object to connect to a database.
  # {'user': 'scala_user', 'password': '', 'host': 'localhost', 'database': 'scala_db'}
  def db_config(self, db_name):
    db = {}
    params = self.config.settings.items(db_name)
    for param in params:
      db[param[0]] = param[1]
    print(db)
    return db

  def app_name_db_passwd(self):
    return self.config.get('app_name_db','password')

def test_query(conn, app_name_db_passwd):
  # Use loan pattern to open a cursor, it'll be automatically closed after exit the scope.
  with conn.cursor() as cur:    
    cur.execute("""select count(*) from version() """)
    rows = cur.fetchall()
    print( "\nShow me the data:\n")
    for row in rows:
        print( "row count:   ", row[0])

def main():
  try:
      app_name_tool = DbTool("/Users/charliezhu/work/blastworks/aws/database.ini")
      app_name_db = app_name_tool.db_config(db_name = 'local_db')
      # Same loan pattern, but for database connection.
      # **app_name_db, unpack dictionary to key value pairs arguments lists.
      # see, https://docs.python.org/3.7/tutorial/controlflow.html#unpacking-argument-lists
      with psycopg2.connect(**app_name_db) as conn:
        test_query(conn, app_name_tool.app_name_db_passwd())
  except:
      traceback.print_exc()
      print("I am unable to connect to the database")

#  if run as the single script, run main method.
if __name__ == '__main__':
  main()
