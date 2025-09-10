import numpy as np
import pandas as pd

def session_summaries(df: pd.DataFrame):
    df["date_label"] = df["date"].rank(method="dense").astype(int)
    return df

def basic_stats(df: pd.DataFrame):
    df["volume"] = df["sets"] * df["reps"] * df["weight"]
    result = df.groupby("exercise").agg({
        "volume": "sum",
        "sets": "sum",
        "weight": ["max", "mean"]
        }).reset_index()
    result.columns = ["exercise", "total_volume", "total_sets", "max_weight", "avg_weight"]

    return result

def high_finder(df: pd.DataFrame):
    max_weight = df.groupby("exercise")["weight"].max()
    return max_weight
    