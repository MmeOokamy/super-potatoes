import os
import psycopg2

from config import config

def log(user_id, user_name, task_id, item_id, action, requete):
    # user_id task_id item_id action requete 
    sql = """INSERT INTO logs (user_id, user_name, task_id, item_id, action, requete)
    values (%s, %s, %s, %s, %s, %s)"""
    connexion = None
    try:
        params = config()
        connexion = psycopg2.connect(**params)
        cursor = connexion.cursor()
        cursor.execute(sql, (user_id, user_name, task_id, item_id, action, requete,))
        connexion.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print("error : " + str(error))
    finally:
        if connexion is not None:
            connexion.close()