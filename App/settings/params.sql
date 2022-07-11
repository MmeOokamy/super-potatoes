-- table des preferences
-- CREATE TABLE settings (
--     id SERIAL PRIMARY KEY UNIQUE,
--     setting_parameter VARCHAR(100) NOT NULL,
--     setting_module VARCHAR(100),
--     setting_commentary TEXT,
--     setting_default_value SMALLINT DEFAULT 1 NOT NULL,
--     setting_value SMALLINT DEFAULT 1 NOT NULL
-- );

INSERT INTO settings (setting_parameter, setting_module, setting_commentary,setting_default_value , setting_value)
VALUES 
('Visitor_archyves','Ookarchyves','Permet au visiteur de voir et d''acceder au menu Archyves', 1, 0),
('Visitor_manager','Ookamanager','Permet au visiteur de voir et d''acceder au menu Manager',0 ,1);