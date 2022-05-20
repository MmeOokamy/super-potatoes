-- module d'Ookarchyves
CREATE TABLE ookarchyves_themes (
    id SERIAL PRIMARY KEY UNIQUE,
    theme_title VARCHAR(50),
    theme_description TEXT,
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
