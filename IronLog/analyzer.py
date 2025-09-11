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
    result["avg_intensity"] = result["avg_weight"] / result["max_weight"]
    return result