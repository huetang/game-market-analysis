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

    console_platforms["platform_type"] = "Console"

    pc_platform = pd.DataFrame(
        {
            "platform_name": ["PC"],
            "platform_type": ["PC"]
        }
    )

    platforms = pd.concat(
        [console_platforms, pc_platform],
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