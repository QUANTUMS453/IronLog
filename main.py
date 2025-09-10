import numpy as np
import pandas as pd
from IronLog.loader import load_data, clean_data
from IronLog.analyzer import basic_stats, high_finder

def main():
    raw = load_data(r"D:\IronLog project\IronLog\Data\Workout_Data.csv")
    print("[OK] Loaded data", raw)
    
    df = clean_data(raw)
    print("[Ok], cleaned", df.shape)
    print(df)

    stats = basic_stats(df)
    print("[OK], stats\n", stats)
    
    maxi = high_finder(df)
    print("[OK], the max for each exercise", maxi)



if __name__ == "__main__":
    main()