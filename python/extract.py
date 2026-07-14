import pandas as pd


def extract_vgchartz():
    return pd.read_csv(
        "../data/cleaned/vgchartz_cleaned.csv"
    )


def extract_steam():
    return pd.read_csv(
        "../data/cleaned/steam_cleaned.csv"
    )