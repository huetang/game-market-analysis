
CREATE TABLE Publisher (
    publisher_id INTEGER PRIMARY KEY,
    publisher_name VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE Developer (
    developer_id INTEGER PRIMARY KEY,
    developer_name VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE Genre (
    genre_id INTEGER PRIMARY KEY,
    genre_name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE Platform (
    platform_id INTEGER PRIMARY KEY,
    platform_name VARCHAR(100) NOT NULL UNIQUE,
    platform_type VARCHAR(50) NOT NULL
);

CREATE TABLE Game (
    game_id INTEGER PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    release_date DATE,
    publisher_id INTEGER,
    developer_id INTEGER,
    genre_id INTEGER,

    FOREIGN KEY (publisher_id) REFERENCES Publisher(publisher_id),
    FOREIGN KEY (developer_id) REFERENCES Developer(developer_id),
    FOREIGN KEY (genre_id) REFERENCES Genre(genre_id)
);

CREATE TABLE Game_Release (
    release_id INTEGER PRIMARY KEY,
    game_id INTEGER NOT NULL,
    platform_id INTEGER NOT NULL,
    platform_release_date DATE,

    FOREIGN KEY (game_id) REFERENCES Game(game_id),
    FOREIGN KEY (platform_id) REFERENCES Platform(platform_id)
);

CREATE TABLE Sales (
    sales_id INTEGER PRIMARY KEY,
    release_id INTEGER NOT NULL,
    total_sales DECIMAL(10,2),
    north_america_sales DECIMAL(10,2),
    europe_sales DECIMAL(10,2),
    japan_sales DECIMAL(10,2),
    other_sales DECIMAL(10,2),
    critic_score DECIMAL(3,1),

    FOREIGN KEY (release_id) REFERENCES Game_Release(release_id)
);

CREATE TABLE Steam_Metrics (
    steam_metric_id INTEGER PRIMARY KEY,
    game_id INTEGER NOT NULL,
    steam_app_id INTEGER,
    estimated_owners VARCHAR(50),
    peak_ccu INTEGER,
    price DECIMAL(10,2),
    positive_reviews INTEGER,
    negative_reviews INTEGER,
    average_playtime INTEGER,
    metacritic_score INTEGER,

    FOREIGN KEY (game_id) REFERENCES Game(game_id)
);

CREATE TABLE Price_History (
    price_history_id INTEGER PRIMARY KEY,
    game_id INTEGER NOT NULL,
    store_name VARCHAR(100),
    date DATE,
    price DECIMAL(10,2),
    discount_percentage DECIMAL(5,2),

    FOREIGN KEY (game_id) REFERENCES Game(game_id)
);