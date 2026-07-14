# Data Dictionary

---

# Game

Stores the core information for each unique video game.

| Column | Data Type | Key | Description | Source |
|---------|-----------|-----|-------------|--------|
| game_id | INT | PK | Unique game identifier |  |
| title | VARCHAR(255) | | Game title | VGChartz/Steam |
| release_date | DATE | | Original release date | VGChartz/Steam |
| publisher_id | INT | FK | References Publisher table |  |
| developer_id | INT | FK | References Developer table |  |
| genre_id | INT | FK | References Genre table |  |

---

# Publisher

Stores unique game publishers.

| Column | Data Type | Key | Description |
|---------|-----------|-----|-------------|
| publisher_id | INT | PK | Unique publisher identifier |
| publisher_name | VARCHAR(255) | | Publisher name |

---

# Developer

Stores unique game developers.

| Column | Data Type | Key | Description |
|---------|-----------|-----|-------------|
| developer_id | INT | PK | Unique developer identifier |
| developer_name | VARCHAR(255) | | Developer name |

---

# Genre

Stores unique game genres.

| Column | Data Type | Key | Description |
|---------|-----------|-----|-------------|
| genre_id | INT | PK | Unique genre identifier |
| genre_name | VARCHAR(100) | | Genre name |

---

# Platform

Stores gaming platforms.

| Column | Data Type | Key | Description |
|---------|-----------|-----|-------------|
| platform_id | INT | PK | Unique platform identifier |
| platform_name | VARCHAR(100) | | Platform name |
| platform_type | VARCHAR(50) | | Console or PC |

---

# Game_Release

Represents a specific game released on a specific platform.

| Column | Data Type | Key | Description | Source |
|---------|-----------|-----|-------------|--------|
| release_id | INT | PK | Unique release identifier |  |
| game_id | INT | FK | References Game table |  |
| platform_id | INT | FK | References Platform table |  |
| platform_release_date | DATE | | Platform release date | VGChartz/Steam |

---

# Sales

Stores commercial performance for a game release.

| Column | Data Type | Key | Description | Source |
|---------|-----------|-----|-------------|--------|
| sales_id | INT | PK | Unique sales record |  |
| release_id | INT | FK | References Game_Release table |  |
| total_sales | DECIMAL(10,2) | | Worldwide sales (millions) | VGChartz |
| north_america_sales | DECIMAL(10,2) | | North America sales | VGChartz |
| europe_sales | DECIMAL(10,2) | | Europe sales | VGChartz |
| japan_sales | DECIMAL(10,2) | | Japan sales | VGChartz |
| other_sales | DECIMAL(10,2) | | Other regions sales | VGChartz |
| critic_score | DECIMAL(3,1) | | Critic score | VGChartz |

---

# Steam_Metrics

Stores Steam metrics.

| Column | Data Type | Key | Description | Source |
|---------|-----------|-----|-------------|--------|
| steam_metric_id | INT | PK | Unique Steam metrics identifier |  |
| game_id | INT | FK | References Game table |  |
| steam_app_id | INT | | Steam application ID | Steam |
| estimated_owners | VARCHAR(50) | | Estimated ownership range | Steam |
| peak_ccu | INT | | Peak concurrent users | Steam |
| price | DECIMAL(10,2) | | Current Steam price at the time the dataset was collected | Steam |
| positive_reviews | INT | | Positive review count | Steam |
| negative_reviews | INT | | Negative review count | Steam |
| average_playtime | INT | | Average lifetime playtime (minutes) | Steam |
| metacritic_score | INT | | Metacritic score | Steam |

---

# Price_History

Stores historical pricing and discount information.

| Column | Data Type | Key | Description | Source |
|---------|-----------|-----|-------------|--------|
| price_history_id | INT | PK | Unique price record |  |
| game_id | INT | FK | References Game table |  |
| store_name | VARCHAR(100) | | Store offering the price | IsThereAnyDeal |
| date | DATE | | Date of recorded price | IsThereAnyDeal |
| price | DECIMAL(10,2) | | Sale price | IsThereAnyDeal |
| discount_percentage | DECIMAL(5,2) | | Discount percentage | IsThereAnyDeal |

---

# Entity Relationships

- One Publisher can publish many Games.
- One Developer can develop many Games.
- One Genre can contain many Games.
- One Game can have many platform releases.
- One Platform can contain many game releases.
- One Game Release can have one associated sales record.
- One Game can have one Steam metrics record.
- One Game can have many historical price records.