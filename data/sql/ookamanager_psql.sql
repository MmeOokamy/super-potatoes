-- module Ookamanager Kanban Project
CREATE TABLE ookamanager_modules (
    id SERIAL PRIMARY KEY UNIQUE,
    module_name VARCHAR(255) NOT NULL,
    module_visible SMALLINT DEFAULT 1,
    module_color VARCHAR(30)
);

CREATE TABLE ookamanager_steps (
    id SERIAL PRIMARY KEY UNIQUE,
    step_name VARCHAR(255) NOT NULL,
    step_order INTEGER,
    step_visible SMALLINT DEFAULT 1,
    step_color VARCHAR(30)
);

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
    id SERIAL PRIMARY KEY UNIQUE,
    item_name VARCHAR(255) NOT NULL,
    item_description TEXT,
    item_task_id INTEGER,
    item_status_id SMALLINT DEFAULT 1,
    visible SMALLINT DEFAULT 1,
    FOREIGN KEY (item_task_id) REFERENCES ookamanager_tasks(id),
    FOREIGN KEY (item_status_id) REFERENCES  ookamanager_status(id)
);

