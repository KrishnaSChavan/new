import time
from psycopg2.extras import RealDictCursor
import psycopg2
from .config import settings
import openai
from .config import settings


while True:
    
    try:
        conn = psycopg2.connect(host = f'{settings.database_hostname}',database='fastapi',user=f'{settings.database_username}',password=f'{settings.database_password}',cursor_factory=RealDictCursor)#(host, databatse, user, password,RealDictCursor for obtaining colums of table)
        cursor = conn.cursor()
        print ("Connected")
        break
    except Exception as e:
        print ("Failed to connect")
        print(e)
        time.sleep(5)


openai.api_key = settings.api_key

