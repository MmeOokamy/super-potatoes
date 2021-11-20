import psycopg2
from config import config


def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        DROP TABLE IF EXISTS logs CASCADE;
        DROP TABLE IF EXISTS settings CASCADE;
        DROP TABLE IF EXISTS users CASCADE;
        DROP TABLE IF EXISTS ookamanager_modules CASCADE;
        DROP TABLE IF EXISTS ookamanager_steps CASCADE;
        DROP TABLE IF EXISTS ookamanager_status CASCADE;
        DROP TABLE IF EXISTS ookamanager_projects CASCADE;
        DROP TABLE IF EXISTS ookamanager_tasks CASCADE;
        DROP TABLE IF EXISTS ookamanager_task_items CASCADE;
        DROP TABLE IF EXISTS ookarchyves_articles CASCADE;
        DROP TABLE IF EXISTS ookarchyves_themes CASCADE;
        """,
        """
        CREATE TABLE logs (
            id SERIAL PRIMARY KEY UNIQUE,
            log_user_id INTEGER,
            log_user_name VARCHAR(100),
            log_action VARCHAR(50) NOT NULL,
            log_requete TEXT,
            log_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
        """,
        """
        -- table des preferences
        CREATE TABLE settings (
            id SERIAL PRIMARY KEY UNIQUE,
            setting_parameter VARCHAR(100) NOT NULL,
            setting_module VARCHAR(100),
            setting_commentary TEXT,
            setting_default_value SMALLINT DEFAULT 1 NOT NULL,
            setting_value SMALLINT DEFAULT 1 NOT NULL
        ); 

        INSERT INTO settings (setting_parameter, setting_module, setting_commentary,setting_default_value , setting_value)
        VALUES 
        ('Visitor_archyves','Ookarchyves','Permet au visiteur de voir et d''acceder au menu Archyves', 1, 0),
        ('Visitor_manager','Ookamanager','Permet au visiteur de voir et d''acceder au menu Manager',0 ,1);
        """,
        """
        -- Module Authentification
        CREATE TABLE users (
            id SERIAL PRIMARY KEY UNIQUE,
            user_name VARCHAR(50) UNIQUE NOT NULL,
            user_password VARCHAR(200) NOT NULL,
            user_magical_word VARCHAR(50) NOT NULL,
            user_email VARCHAR(80) NOT NULL,
            user_power SMALLINT DEFAULT 1,
            user_token TEXT,
            user_created_on TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            user_last_login TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        );

        -- 
        INSERT INTO users (id, user_name, user_password, user_magical_word, user_email, user_power, user_created_on)
        VALUES (0, 'visitor', 'sha256$qddhRJjpInPFvtgB$95b2af47611b6fb043ba13bfa38ed9d01f36546c90ff82b372b96e1499c49698', 'poop', 'nomail@dot.com', 1, now()),
        (1, 'Ookamy', 'sha256$0UmOnlJRp88WHO8e$0db2aaeffcf732c91ca8471b8069f20be74e5a7044261826347564e3294a1c13', 'licorn', 'ooka@dot.fr', 4, now());
;
        """,
        """
        -- module Project Management
        CREATE TABLE ookamanager_modules (
            id SERIAL PRIMARY KEY UNIQUE,
            module_name VARCHAR(255) NOT NULL,
            module_visible SMALLINT DEFAULT 1,
            module_color VARCHAR(30)
        )
        """,
        """
        CREATE TABLE ookamanager_steps (
            id SERIAL PRIMARY KEY UNIQUE,
            step_name VARCHAR(255) NOT NULL,
            step_order INTEGER,
            step_visible SMALLINT DEFAULT 1,
            step_color VARCHAR(30)
        )
        """,
        """
        CREATE TABLE ookamanager_status (
            id SERIAL PRIMARY KEY UNIQUE,
            status_name VARCHAR(255) NOT NULL,
            status_order INTEGER,
            status_visible SMALLINT DEFAULT 1
        );

        CREATE TABLE ookamanager_projects (
            id SERIAL PRIMARY KEY UNIQUE,
            project_name VARCHAR(50),
            project_description TEXT,
            project_user_id INTEGER,
            project_create_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            project_update_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            project_finish_at TIMESTAMP,
            project_estimation VARCHAR(50),
            project_deadline DATE,
            FOREIGN KEY (project_user_id) REFERENCES users (id)
        );

        CREATE TABLE ookamanager_tasks (
            id SERIAL PRIMARY KEY UNIQUE,
            task_title VARCHAR(255) NOT NULL,
            task_body VARCHAR(255) NOT NULL,
            task_order INTEGER,
            task_project_id INTEGER,
            task_module INTEGER,
            task_deadline VARCHAR(50),
            task_step_id INTEGER NOT NULL DEFAULT 0,
            task_user_id INTEGER NOT NULL,
            task_create_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            task_update_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            task_finish_at TIMESTAMP,
            FOREIGN KEY (task_user_id) REFERENCES users (id),
            FOREIGN KEY (task_project_id) REFERENCES ookamanager_projects (id),
            FOREIGN KEY (task_step_id) REFERENCES ookamanager_steps (id)
        );

        CREATE TABLE ookamanager_task_items (
            id SERIAL PRIMARY KEY UNIQUE,
            item_name VARCHAR(255) NOT NULL,
            item_description TEXT,
            item_task_id INTEGER,
            item_status_id SMALLINT DEFAULT 1,
            visible SMALLINT DEFAULT 1,
            FOREIGN KEY (item_task_id) REFERENCES ookamanager_tasks(id),
            FOREIGN KEY (item_status_id) REFERENCES  ookamanager_status(id)
        );

        -- module d'Ookarchyves
        CREATE TABLE ookarchyves_themes (
            id SERIAL PRIMARY KEY UNIQUE,
            theme_title VARCHAR(50),
            theme_description TEXT,
            theme_private SMALLINT DEFAULT 1
        );

        INSERT INTO ookarchyves_themes (theme_title, theme_description, theme_private) 
        values ('SQL', 'sql, console postgresql', 0),('Linux', 'Manjaro, console, install', 0);


        CREATE TABLE ookarchyves_articles (
            id SERIAL PRIMARY KEY UNIQUE,
            article_title VARCHAR(100),
            article_author_id INTEGER,
            article_create_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            article_update_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            article_body TEXT,
            article_theme_id INTEGER,
            article_private SMAllINT DEFAULT 1,
            FOREIGN KEY (article_theme_id) REFERENCES ookarchyves_themes(id),
            FOREIGN KEY (article_author_id) REFERENCES users(id)
        );
        """
    )

    conn = None
    try:
        # read the connection parameters
        print('Read the connection parameters')
        params = config()
        # connect to the PostgreSQL server
        print('Connect to the PostgreSQL server')
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        print("Create table one by one")
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        print('Close communication with the PostgreSQL database server')
        cur.close()
        # commit the changes
        print('commit the changes')
        conn.commit()
        print("====>  Database has been modified  <====")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Disabled Connection')


if __name__ == '__main__':
    create_tables()
