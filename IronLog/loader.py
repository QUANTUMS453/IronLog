import numpy as np
import pandas as pd

def load_data(path: str):
    df = pd.read_csv(path)
    main_df = pd.DataFrame(df)

def clean_data(main_df):
    df = main_df.copy()

    #sorting dates
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date")

    #normalizing exercise names
    df["exercise"] = df["exercise"].str.lower().str.replace(" ", "_")
    
    #ensuring numeric types in data
    df[["sets", "reps", "weight"]] = df[["sets", "reps", "weight"]].apply(pd.to_numeric, errors="coerce")

    #avoiding NaN or impossible
    df = df.dropna(subset=["sets", "reps", "weight"])
    df = df[(df["sets"] > 0) & (df["reps"] > 0) & (df["weight"] > 0)]

    #removing duplicates
    df = df.drop_duplicates()

    return df


