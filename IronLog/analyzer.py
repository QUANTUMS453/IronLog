import pandas as pd



# Calculates total volume, sets, max/avg weight, and intensity per session.
def summarize(df: pd.DataFrame, by: str):
    df = df.copy()
    df["volume"] = df["sets"] * df["reps"] * df["weight"]
    grouped = df.groupby(by).agg(
        total_volume=pd.NamedAgg(column="volume", aggfunc="sum"),
        total_sets=pd.NamedAgg(column="sets", aggfunc="sum"),
        total_reps=pd.NamedAgg(column="reps", aggfunc="sum"),
        max_weight=pd.NamedAgg(column="weight", aggfunc="max"),
        avg_weight=pd.NamedAgg(column="weight", aggfunc="mean"),
    ).reset_index()
    grouped["avg_intensity"] = grouped["avg_weight"] / grouped["max_weight"]
    return grouped