import numpy as np
import pandas as pd

def load_data(path: str):
    df = pd.read_csv(path)
    main_df = pd.DataFrame(df)

    return main_df


def clean_data(main_df: pd.DataFrame):
    # Standardizing column names
    df = main_df.copy()
    df.columns = df.columns.str.strip().str.lower()

    # Convert all string columns to lower case
    str_cols = df.select_dtypes(include='object').columns
    df[str_cols] = df[str_cols].apply(lambda x: x.str.lower())

    #sorting dates
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date")

    #normalizing exercise names
    df["exercise"] = df["exercise"].str.replace(" ", "_")
    
    #ensuring numeric types in data
    df[["sets", "reps", "weight"]] = df[["sets", "reps", "weight"]].apply(pd.to_numeric, errors="coerce")

    #avoiding NaN or impossible
    df = df.dropna(subset=["sets", "reps", "weight"])
    df = df[(df["sets"] > 0) & (df["reps"] > 0) & (df["weight"] > 0)]

    #removing duplicates
    df = df.drop_duplicates()

    return df


