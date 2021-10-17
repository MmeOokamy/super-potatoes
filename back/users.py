import os
import psycopg2
from werkzeug.security import generate_password_hash, check_password_hash

from db import MyDatabase
import log

def users_list():
    sql = """ 
        SELECT * FROM users;
        """
    got_it = False
    users_list = []

    try:
        # params = config()
        # connexion = psycopg2.connect(**params)
        # cursor = connexion.cursor()
        # cursor.execute(sql)

        response = cursor.fetchall()
        for user in response:
            user_dict = {}
            user_dict.update({'id': user[0]})
            user_dict.update({'user_name': user[1]})
            user_dict.update({'user_password': user[2]})
            user_dict.update({'user_email': user[3]})
            user_dict.update({'user_power': user[4]})
            users_list.append(user_dict)
        connexion.commit()
        cursor.close()
        return users_list

    except (Exception, psycopg2.DatabaseError) as error:
        print("error : " + str(error))
    finally:
        if connexion is not None:
            connexion.close()
    return got_it


def create_user(user_name, user_password, user_email):
    sql = """ 
        INSERT INTO users (user_name, user_password, user_email, user_power) 
        VALUES (%s,%s,%s, 1);
        """
    connexion = None
    h_user_password = generate_password_hash(user_password)
    got_it = False

    try:
        params = config()
        connexion = psycopg2.connect(**params)
        cursor = connexion.cursor()
        cursor.execute(sql, (user_name, h_user_password, user_email,))
        log.log(0, user_name, 0, 0, "create_user", sql)
        connexion.commit()
        got_it = True
        print("it's commit, you are create a new user")
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print("error : " + str(error))
    finally:
        if connexion is not None:
            connexion.close()
    return got_it


if __name__ == '__main__':
    # create_user('ooka', 'root', 'test@mail.fr')
    # create_user('test', 'root', 'test@test.fr')
    # users_list()
    Users.get_users()
