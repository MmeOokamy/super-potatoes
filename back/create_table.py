import psycopg2
from config import config


def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
            DROP TABLE IF EXISTS users CASCADE;
            DROP TABLE IF EXISTS logs CASCADE;
            DROP TABLE IF EXISTS tasks_list CASCADE;
            DROP TABLE IF EXISTS task_items CASCADE;
            DROP TABLE IF EXISTS column_list CASCADE;
            DROP TABLE IF EXISTS status_list CASCADE;
            DROP TABLE IF EXISTS module_list CASCADE;
        """,
        """
        CREATE TABLE logs (
            id SERIAL PRIMARY KEY UNIQUE,
            user_id INTEGER NOT NULL,
            task_id INTEGER,
            item_id INTEGER,
            action VARCHAR(50),
            requete TEXT,
            created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
        """,
        """
        CREATE TABLE module (
            id SERIAL PRIMARY KEY UNIQUE,
            module_name VARCHAR(255) NOT NULL,
            visible SMALLINT DEFAULT 1
        )
        """,
        """
        CREATE TABLE step (
            id SERIAL PRIMARY KEY UNIQUE,
            step_name VARCHAR(255) NOT NULL,
            step_order INTEGER,
            visible SMALLINT DEFAULT 1
        )
        """,
        """
        CREATE TABLE status (
            id SERIAL PRIMARY KEY UNIQUE,
            status_name VARCHAR(255) NOT NULL,
            status_order INTEGER,
            visible SMALLINT DEFAULT 1
        )
        """,
        """
        CREATE TABLE users (
            id SERIAL PRIMARY KEY UNIQUE,
            user_name VARCHAR(100) UNIQUE NOT NULL,
            user_password VARCHAR(255) NOT NULL,
            user_email VARCHAR(255) NOT NULL,
            user_power SMALLINT DEFAULT 1
        )
        """,
        """
        CREATE TABLE tasks (
            id SERIAL PRIMARY KEY UNIQUE,
            task_title VARCHAR(255) NOT NULL,
            task_body VARCHAR(255) NOT NULL,
            task_order INTEGER,
            task_module INTEGER,
            task_step_id INTEGER NOT NULL DEFAULT 0,
            task_user_id INTEGER NOT NULL,
            task_create_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            task_update_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            task_finish_at TIMESTAMP,
            FOREIGN KEY (task_user_id) REFERENCES users (id),
            FOREIGN KEY (task_step_id) REFERENCES step (id)
        )
        """,
        """
        CREATE TABLE task_items (
            id SERIAL PRIMARY KEY UNIQUE,
            item_name VARCHAR(255) NOT NULL,
            item_description TEXT,
            item_task_id INTEGER,
            item_status_id SMALLINT DEFAULT 1,
            visible SMALLINT DEFAULT 1,
            FOREIGN KEY (item_task_id) REFERENCES tasks (id),
            FOREIGN KEY (item_status_id) REFERENCES  status(id)
        )
        """,
        """
            INSERT INTO users (user_name, user_password, user_email, user_power) VALUES ('ookamy', 'choisir', 'tvst@hotmail.fr', 4);
            INSERT INTO status (status_name, status_order) VALUES ('to do', 1), ('in progress', 2), ('done', 3), ('drop', 4);
            INSERT INTO step (id, step_name, step_order) VALUES (0, 'To Do', 1), (1, 'In Progress', 2), (2, 'In Testing', 3), (3, 'In Review', 4),(4, 'Done', 5), (5, 'Drop', 6);
            INSERT INTO module (module_name) VALUES ('Authentification'), ('Backend'), ('Frontend');
        """
    )

    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
        print("Database has been modified")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_tables()
