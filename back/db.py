from configparser import ConfigParser
import psycopg2
import os 
from dotenv import load_dotenv 


dotenv_path = os.path.join(os.path.dirname(__file__), '.env') 

if os.path.exists(dotenv_path): 
    load_dotenv(dotenv_path)

from config import config

class MyDatabase():
    def __init__(self):
        param = config()
        self.conn = psycopg2.connect(**param)
        self.cur = self.conn.cursor()


    def query(self, query):
        self.cur.execute(query)
        self.conn.commit()

    
    def close(self):
        self.cur.close()
        self.conn.close()


if __name__ == '__main__':
    db = MyDatabase()
    # db.query('select * from users;')
    db.query("INSERT INTO step (step_name, step_order) VALUES ('Destruction', 10)")
    db.close()