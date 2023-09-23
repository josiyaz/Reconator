import os
from time import sleep
import psycopg2
import base64

conn = psycopg2.connect(
    host="db",
    database="test_db",
    user="test_user",
    password="test_password"
)

cur = conn.cursor()

#checks the db queue table every 60 secs
while True:
 try:
   cur.execute("select * from queue limit 1")
   t = cur.fetchall()
   t = t[0]
   id = t[0]
   url = t[1]
   conn.commit()
   cur.execute(f"delete from queue where id = '{id}'")
   conn.commit()

   #sends to run.py
   os.system('python run.py {}'.format(url))
   #next scan starts after 1 minute
   sleep(60)

 except:
   sleep(60)

cur.close()
conn.close()
