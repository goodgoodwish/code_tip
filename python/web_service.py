import urllib.request
import json
import psycopg2

def ranks_from_api():
  contents = urllib.request.urlopen("http://localhost:8080/gp").read()
  jsonContent = json.loads(contents.decode('utf-8'))

  ranks = []
  platform = jsonContent["device"]
  app_id = 351804002
  game_name = "Slingo Arcade"
  publisher_id = 20200001614793
  publisher_name = "Blastworks Inc."

  elem = jsonContent['product_ranks'][0]['ranks']

  for x in jsonContent['product_ranks']:
    country_name = x["country"]
    rank_type = x["feed"]
    casino_game = x["category"]
    for rank_date, rank_num in x["ranks"].items() :
      ranks.append((platform, country_name, app_id, game_name, publisher_id, publisher_name
      , rank_date, rank_type, rank_num, casino_game))

  for r in ranks :
    print(r)

  return ranks

def insert_ranks(ranks):
  """ insert multiple rows into a table  """
  sql = """INSERT INTO rank_history_appannie(
  platform      ,
  country_name  ,
  app_id        ,
  game_name     ,
  publisher_id  ,
  publisher_name,
  rank_date     ,
  rank_type     ,
  rank_num      ,
  casino_game ) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
  """
  conn = None
  try:
    # params = config()
    # conn = psycopg2.connect(**params)
    conn = psycopg2.connect(host="localhost",database="scala_db", user="scala_user")
    cur = conn.cursor() 
    cur.executemany(sql, ranks) 
    conn.commit()
    cur.close() 
  except (Exception, psycopg2.DatabaseError) as error: 
    print(error) 
  finally:
    if conn is not None:
      conn.close() 

if __name__ == '__main__':
  ranks = ranks_from_api()
  insert_ranks(ranks)
