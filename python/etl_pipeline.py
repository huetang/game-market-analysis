from extract import extract_vgchartz, extract_steam

from transform import (
    create_publishers,
    create_developers,
    create_genres,
    create_platforms,
    create_games,
    create_game_releases
)

from load import load_dataframe

def run_etl():

    vg = extract_vgchartz()
    steam = extract_steam()

    publishers = create_publishers(vg)
    developers = create_developers(vg)
    genres = create_genres(vg)
    platforms = create_platforms(vg, steam)
    games = create_games(
        vg,
        publishers,
        developers,
        genres)
    game_releases = create_game_releases(
        vg,
        steam,
        games,
        platforms)

    print("Game Releases")
    print(game_releases.head())
    load_dataframe(publishers, "Publisher")
    load_dataframe(developers, "Developer")
    load_dataframe(genres, "Genre")
    load_dataframe(platforms, "Platform")
    load_dataframe(games,"Game")
    load_dataframe(game_releases,"Game_Release")

run_etl()