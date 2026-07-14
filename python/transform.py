import pandas as pd


def create_publishers(vg):

    publishers = (
        vg["publisher"]
        .dropna()
        .drop_duplicates()
        .sort_values()
        .reset_index(drop=True)
        .to_frame(name="publisher_name")
    )

    publishers["publisher_id"] = publishers.index + 1

    return publishers[
        [
            "publisher_id",
            "publisher_name"
        ]
    ]


def create_developers(vg):

    developers = (
        vg["developer"]
        .dropna()
        .drop_duplicates()
        .sort_values()
        .reset_index(drop=True)
        .to_frame(name="developer_name")
    )

    developers["developer_id"] = developers.index + 1

    return developers[
        [
            "developer_id",
            "developer_name"
        ]
    ]


def create_genres(vg):

    genres = (
        vg["genre"]
        .dropna()
        .drop_duplicates()
        .sort_values()
        .reset_index(drop=True)
        .to_frame(name="genre_name")
    )

    genres["genre_id"] = genres.index + 1

    return genres[
        [
            "genre_id",
            "genre_name"
        ]
    ]


def create_platforms(vg, steam):

    console_platforms = (
        vg["console"]
        .dropna()
        .drop_duplicates()
        .sort_values()
        .reset_index(drop=True)
        .to_frame(name="platform_name")
    )

    #remove PC to classify as PC console type later
    console_platforms = console_platforms[
        console_platforms["platform_name"].str.upper() != "PC"
    ]

    console_platforms["platform_type"] = "Console"


    pc_platform = pd.DataFrame(
        {
            "platform_name": ["PC"],
            "platform_type": ["PC"]
        }
    )


    platforms = pd.concat(
        [
            console_platforms,
            pc_platform
        ],
        ignore_index=True
    )


    platforms = (
        platforms
        .drop_duplicates(subset="platform_name")
        .reset_index(drop=True)
    )


    platforms["platform_id"] = platforms.index + 1


    return platforms[
        [
            "platform_id",
            "platform_name",
            "platform_type"
        ]
    ]


def create_games(vg, publishers, developers, genres):

    games = vg[
        [
            "title",
            "release_date",
            "publisher",
            "developer",
            "genre"
        ]
    ].copy()


    games = (
        games
        .drop_duplicates(subset="title")
        .reset_index(drop=True)
    )

    games = games.merge(
        publishers,
        left_on="publisher",
        right_on="publisher_name",
        how="left"
    )


    games = games.merge(
        developers,
        left_on="developer",
        right_on="developer_name",
        how="left"
    )


    games = games.merge(
        genres,
        left_on="genre",
        right_on="genre_name",
        how="left"
    )

    games["game_id"] = games.index + 1

    return games[
        [
            "game_id",
            "title",
            "release_date",
            "publisher_id",
            "developer_id",
            "genre_id"
        ]
    ]

def create_game_releases(vg, steam, games, platforms):

    vg_releases = vg[
        [
            "title",
            "console",
            "release_date"
        ]
    ].copy()

    vg_releases = vg_releases.merge(
        games[["game_id", "title"]],
        on="title",
        how="left"
    )

    vg_releases = vg_releases.merge(
        platforms[
            [
                "platform_id",
                "platform_name"
            ]
        ],
        left_on="console",
        right_on="platform_name",
        how="left"
    )

    vg_releases = vg_releases.rename(
        columns={
            "release_date": "platform_release_date"
        }
    )

    vg_releases = vg_releases[
        [
            "game_id",
            "platform_id",
            "platform_release_date"
        ]
    ]


    steam_releases = steam[
        [
            "name",
            "release_date"
        ]
    ].copy()

    steam_releases = steam_releases.rename(
        columns={
            "name": "title"
        }
    )

    steam_releases = steam_releases.merge(
        games[
            [
                "game_id",
                "title"
            ]
        ],
        on="title",
        how="inner"
    )

    pc_platform = platforms.loc[
        platforms["platform_name"] == "PC",
        "platform_id"
    ].iloc[0]

    steam_releases["platform_id"] = pc_platform

    steam_releases = steam_releases.rename(
        columns={
            "release_date": "platform_release_date"
        }
    )

    steam_releases = steam_releases[
        [
            "game_id",
            "platform_id",
            "platform_release_date"
        ]
    ]


    releases = pd.concat(
        [
            vg_releases,
            steam_releases
        ],
        ignore_index=True
    )

    releases = (
        releases
        .drop_duplicates()
        .reset_index(drop=True)
    )

    releases["release_id"] = releases.index + 1

    return releases[
        [
            "release_id",
            "game_id",
            "platform_id",
            "platform_release_date"
        ]
    ]

def create_sales(vg, games, platforms, game_releases):

    sales = vg[
        [
            "title",
            "console",
            "release_date",
            "critic_score",
            "total_sales",
            "na_sales",
            "jp_sales",
            "pal_sales",
            "other_sales"
        ]
    ].copy()


    sales = sales.merge(
        games[["game_id", "title"]],
        on="title",
        how="left"
    )

    sales = sales.merge(
        platforms[["platform_id", "platform_name"]],
        left_on="console",
        right_on="platform_name",
        how="left"
    )

    sales = sales.merge(
        game_releases[
            [
                "release_id",
                "game_id",
                "platform_id",
                "platform_release_date"
            ]
        ],
        left_on=[
            "game_id",
            "platform_id",
            "release_date"
        ],
        right_on=[
            "game_id",
            "platform_id",
            "platform_release_date"
        ],
        how="left"
    )

    sales = sales.rename(
        columns={
            "na_sales": "north_america_sales",
            "pal_sales": "europe_sales",
            "jp_sales": "japan_sales"
        }
    )

    sales["sales_id"] = sales.index + 1

    return sales[
        [
            "sales_id",
            "release_id",
            "total_sales",
            "north_america_sales",
            "europe_sales",
            "japan_sales",
            "other_sales",
            "critic_score"
        ]
    ]

def create_steam_metrics(steam, games):

    metrics = steam[
        [
            "appid",
            "name",
            "estimated_owners",
            "peak_ccu",
            "price",
            "positive",
            "negative",
            "average_playtime_forever",
            "metacritic_score"
        ]
    ].copy()


    metrics = metrics.merge(
        games[
            [
                "game_id",
                "title"
            ]
        ],
        left_on="name",
        right_on="title",
        how="inner"
    )


    metrics = metrics.rename(
        columns={
            "appid": "steam_app_id",
            "positive": "positive_reviews",
            "negative": "negative_reviews",
            "average_playtime_forever": "average_playtime"
        }
    )


    metrics["steam_metric_id"] = metrics.index + 1


    return metrics[
        [
            "steam_metric_id",
            "game_id",
            "steam_app_id",
            "estimated_owners",
            "peak_ccu",
            "price",
            "positive_reviews",
            "negative_reviews",
            "average_playtime",
            "metacritic_score"
        ]
    ]