import numpy as np
import pandas as pd


def basic_stats(df: pd.DataFrame):
    df["volume"] = df["sets"] * df["reps"] * df["weight"]
    result = df.groupby("exercise")["volume"].sum().reset_index()

    return result

def high_finder(df: pd.DataFrame):
    max_weight = df.groupby("exercise")["weight"].max()

    return max_weight
