import os
import psycopg2

from config import config

"""
A voir pour faire un trigger directement sur la psql
"""


def logs(user_id, user_name, action, requete):
    # user_id task_id item_id action requete
    sql = """INSERT INTO logs (log_user_id, log_user_name, log_action, log_requete)
               VALUES (%s, %s, %s, %s)
            """
    connexion = None
    try:
        params = config()
        connexion = psycopg2.connect(**params)
        cursor = connexion.cursor()
        cursor.execute(sql, (user_id, user_name, action, requete,))
        connexion.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print("error : " + str(error))
    finally:
        if connexion is not None:
            connexion.close()
