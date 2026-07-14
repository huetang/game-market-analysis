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