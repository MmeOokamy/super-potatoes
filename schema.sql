DROP TABLE IF EXISTS logs CASCADE;
DROP TABLE IF EXISTS settings CASCADE;
DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS project_management_modules CASCADE;
DROP TABLE IF EXISTS project_management_steps CASCADE;
DROP TABLE IF EXISTS project_management_status CASCADE;
DROP TABLE IF EXISTS project_management_projects CASCADE;
DROP TABLE IF EXISTS project_management_tasks CASCADE;
DROP TABLE IF EXISTS project_management_task_items CASCADE;
DROP TABLE IF EXISTS ookarchyves_themes CASCADE;
DROP TABLE IF EXISTS ookarchyves_articles CASCADE;

-- Log
CREATE TABLE logs (
    id SERIAL PRIMARY KEY UNIQUE,
    log_user_id INTEGER,
    log_user_name VARCHAR(100),
    log_action VARCHAR(50) NOT NULL,
    log_requete TEXT,
    log_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);


-- table des preferences
CREATE TABLE settings (
    id SERIAL PRIMARY KEY UNIQUE,
    setting_parameter VARCHAR(100) NOT NULL,
    setting_module VARCHAR(100),
    setting_commentary TEXT,
    setting_default_value SMALLINT DEFAULT 1 NOT NULL,
    setting_value SMALLINT DEFAULT 1 NOT NULL
);

-- Module Authentification

CREATE TABLE users (
    id SERIAL PRIMARY KEY UNIQUE,
    user_name VARCHAR(100) UNIQUE NOT NULL,
    user_password VARCHAR(255) NOT NULL,
    user_email VARCHAR(255) NOT NULL,
    user_power SMALLINT DEFAULT 1,
    user_token TEXT
);

INSERT INTO users (id, user_name, user_password, user_email, user_power)
VALUES (0, 'visitor', 'pbkdf2:sha256:260000$bSxyWsvIkwwNAaVi$b260f5bd6e1539ccc1a8fd279c9dc1167de1f7fa383525fd10a47d5eca1b65e0', 'nomail@dot.com', 1);

-- module Project Management
CREATE TABLE project_management_modules (
    id SERIAL PRIMARY KEY UNIQUE,
    module_name VARCHAR(255) NOT NULL,
    module_visible SMALLINT DEFAULT 1,
    module_color VARCHAR(10)
);

CREATE TABLE project_management_steps (
    id SERIAL PRIMARY KEY UNIQUE,
    step_name VARCHAR(255) NOT NULL,
    step_order INTEGER,
    step_visible SMALLINT DEFAULT 1,
    step_color VARCHAR(10)
);

CREATE TABLE project_management_status (
    id SERIAL PRIMARY KEY UNIQUE,
    status_name VARCHAR(255) NOT NULL,
    status_order INTEGER,
    status_visible SMALLINT DEFAULT 1
);

CREATE TABLE project_management_projects (
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

CREATE TABLE project_management_tasks (
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
    FOREIGN KEY (task_project_id) REFERENCES project_management_projects (id),
    FOREIGN KEY (task_step_id) REFERENCES project_management_steps (id)
);

CREATE TABLE project_management_task_items (
    id SERIAL PRIMARY KEY UNIQUE,
    item_name VARCHAR(255) NOT NULL,
    item_description TEXT,
    item_task_id INTEGER,
    item_status_id SMALLINT DEFAULT 1,
    visible SMALLINT DEFAULT 1,
    FOREIGN KEY (item_task_id) REFERENCES project_management_tasks(id),
    FOREIGN KEY (item_status_id) REFERENCES  project_management_status(id)
);

-- module d'Ookarchyves
CREATE TABLE ookarchyves_themes (
    id SERIAL PRIMARY KEY UNIQUE,
    theme_title VARCHAR(50),
    theme_private SMALLINT DEFAULT 1
);

CREATE TABLE ookarchyves_articles (
    id SERIAL PRIMARY KEY UNIQUE,
    article_title VARCHAR(100),
    article_author_id INTEGER,
    article_create_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    article_update_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    article_body TEXT,
    article_theme_id INTEGER,
    article_private SMALLINT DEFAULT 1,
    FOREIGN KEY (article_theme_id) REFERENCES ookarchyves_themes(id),
    FOREIGN KEY (article_author_id) REFERENCES users(id)
);
