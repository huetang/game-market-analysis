from extract import extract_vgchartz, extract_steam

from transform import (
    create_publishers,
    create_developers,
    create_genres,
    create_platforms,
    create_games,
    create_game_releases,
    create_sales,
    create_steam_metrics
)

from load import load_dataframe

def run_etl():

    vg = extract_vgchartz()
    steam = extract_steam()
    vg = vg[vg["console"] != "Series"].copy() #not individual game releases
    vg = vg[vg["console"] != "All"].copy()
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
    sales = create_sales(
        vg,
        games,
        platforms,
        game_releases
    )
    steam_metrics = create_steam_metrics(
    steam,
    games
)
    print(
    len(steam_metrics),
    "Steam games matched"
)
    print("Steam Metrics")
    print(steam_metrics.head())
    load_dataframe(publishers, "Publisher")
    load_dataframe(developers, "Developer")
    load_dataframe(genres, "Genre")
    load_dataframe(platforms, "Platform")
    load_dataframe(games,"Game")
    load_dataframe(game_releases,"Game_Release")
    load_dataframe(sales,"Sales")
    load_dataframe(steam_metrics,"Steam_Metrics")
run_etl()