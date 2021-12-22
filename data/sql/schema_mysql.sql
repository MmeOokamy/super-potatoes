-- SQL
-- Purge des tables

DROP TABLE IF EXISTS logs;
DROP TABLE IF EXISTS settings;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS ookamanager_modules;
DROP TABLE IF EXISTS ookamanager_steps;
DROP TABLE IF EXISTS ookamanager_status;
DROP TABLE IF EXISTS ookamanager_projects;
DROP TABLE IF EXISTS ookamanager_tasks;
DROP TABLE IF EXISTS ookamanager_task_items;
DROP TABLE IF EXISTS ookarchyves_themes;
DROP TABLE IF EXISTS ookarchyves_articles;

-- Log
CREATE TABLE logs (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    log_user_id INTEGER,
    log_user_name VARCHAR(100),
    log_action VARCHAR(50) NOT NULL,
    log_requete TEXT,
    log_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- table des preferences
CREATE TABLE settings (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    setting_parameter VARCHAR(100) NOT NULL,
    setting_module VARCHAR(100),
    setting_commentary TEXT,
    setting_default_value SMALLINT DEFAULT 1 NOT NULL,
    setting_value SMALLINT DEFAULT 1 NOT NULL
);

-- Module Authentification
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    user_name VARCHAR(50) UNIQUE NOT NULL,
    user_password VARCHAR(200) NOT NULL,
    user_magical_word VARCHAR(50) NOT NULL,
    user_email VARCHAR(80) NOT NULL,
    user_power SMALLINT DEFAULT 1,
    user_token TEXT,
    user_created_on TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    user_last_login TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);


-- module Ookamanager Kanban Project
CREATE TABLE ookamanager_modules (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    module_name VARCHAR(255) NOT NULL,
    module_visible SMALLINT DEFAULT 1,
    module_color VARCHAR(30)
);

CREATE TABLE ookamanager_steps (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    step_name VARCHAR(255) NOT NULL,
    step_order INTEGER,
    step_visible SMALLINT DEFAULT 1,
    step_color VARCHAR(30)
);

CREATE TABLE ookamanager_status (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    status_name VARCHAR(255) NOT NULL,
    status_order INTEGER,
    status_visible SMALLINT DEFAULT 1
);

CREATE TABLE ookamanager_projects (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
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
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    task_title VARCHAR(255) NOT NULL,
    task_body TEXT,
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
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
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
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    theme_title VARCHAR(50),
    theme_description TEXT,
    theme_private SMALLINT DEFAULT 1
);


CREATE TABLE ookarchyves_articles (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
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
