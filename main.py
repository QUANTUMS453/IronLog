from IronLog.loader import load_data, clean_data
from IronLog.analyzer import summarize
from IronLog.visualizer import data_visualizer
from pathlib import Path

def main():
    raw = load_data(Path("Data")/"Workout_Data2.csv")
    print("[OK] Loaded data", raw)
    
    df = clean_data(raw)
    print("[Ok], cleaned", df.shape)
    print(df)

    session_summary = summarize(df, by="date")
    print("[OK] Summarized data\n", session_summary)

    excercise_summary = summarize(df, by="exercise")
    print("[OK] Summarized data\n", excercise_summary)

    plot1 = data_visualizer(excercise_summary)
    plot1.savefig("exercise_summary.png")


if __name__ == "__main__":
    main()