import time
from psycopg2.extras import RealDictCursor
import psycopg2

while True:
    
    try:
        conn = psycopg2.connect(host = 'localhost',database='fastapi1',user='abc',password='-',cursor_factory=RealDictCursor)#(host, databatse, user, password,RealDictCursor for obtaining colums of table)
        cursor = conn.cursor()
        print ("Connected")
        break
    except Exception as e:
        print ("Failed to connect")
        print(e)
        time.sleep(5)

