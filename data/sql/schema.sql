
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
    user_name VARCHAR(50) UNIQUE NOT NULL,
    user_password VARCHAR(200) NOT NULL,
    user_magical_word VARCHAR(50) NOT NULL,
    user_email VARCHAR(80) NOT NULL,
    user_power SMALLINT DEFAULT 1,
    user_token TEXT,
    user_created_on TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    user_last_login TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);


