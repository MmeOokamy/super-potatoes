INSERT INTO ookamanager_modules (module_name, module_color)
VALUES ('Ookamanager', 'red darken-4'),('Ookarchyves', 'purple darken-3');

INSERT INTO ookamanager_steps (step_name, step_order, step_color)
VALUES ('a faire', 1,'cyan lighten-3'), ('en cours', 2,'orange darken-2'), ('Terminer', 3,'light-green lighten-3');

INSERT INTO ookamanager_status(status_name, status_order)
VALUES ('a faire', 1), ('en conception', 2), ('en developpement', 3), ('en teste', 4), ('fini', 5);

INSERT INTO settings (setting_parameter, setting_module, setting_commentary,setting_default_value , setting_value)
VALUES ('Visitor_archyves','Ookarchyves','Permet au visiteur de voir et d''acceder au menu Archyves', 1, 0),
('Visitor_manager','Ookamanager','Permet au visiteur de voir et d''acceder au menu Manager',0 ,1);

INSERT INTO users (id, user_name, user_password, user_magical_word, user_email, user_power, user_created_on)
VALUES (0, 'visitor', 'sha256$qddhRJjpInPFvtgB$95b2af47611b6fb043ba13bfa38ed9d01f36546c90ff82b372b96e1499c49698', 'poop', 'nomail@dot.com', 1, now()),
(1, 'Ookamy', 'sha256$0UmOnlJRp88WHO8e$0db2aaeffcf732c91ca8471b8069f20be74e5a7044261826347564e3294a1c13', 'licorn', 'ooka@dot.fr', 4, now());

-- theme
INSERT INTO ookarchyves_themes (theme_title, theme_description, theme_private) 
values ('Nouveaute', 'les dernieres nouveaute sur le site /!\ cela peut etre affiche sur le page index', 0),('SQL', 'sql, console postgresql', 0),('Linux', 'Manjaro, console, install', 0);
