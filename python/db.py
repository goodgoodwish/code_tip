import psycopg2
import traceback

import sys
sys.path.insert(0,"/Users/abc/git/cloud/etl")
from etl.pipeline_core.config import Config

class DbTool(object):
  # def __init__() # put config setter here?
  config = Config.load("/Users/abc/aws/database.ini")

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
  with conn.cursor() as cur:    
    cur.execute("""select count(*) from version() """)
    rows = cur.fetchall()
    print( "\nShow me the data:\n")
    for row in rows:
        print( "row count:   ", row[0])

def main():
  try:
      app_name_tool = DbTool()
      app_name_db = app_name_tool.db_config(db_name = 'local_db')
      with psycopg2.connect(**app_name_db) as conn:
        test_query(conn, app_name_tool.app_name_db_passwd())
  except:
      traceback.print_exc()
      print("I am unable to connect to the database")

if __name__ == '__main__':
  main()
