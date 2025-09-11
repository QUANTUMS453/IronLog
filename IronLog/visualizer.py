import pandas as pd
import matplotlib.pyplot as plt


def data_visualizer(df: pd.DataFrame):
    plt.bar(df["exercise"], df["total_volume"], color="skyblue")
    plt.title("Total Volume per Exercise")
    plt.xlabel("Exercise")
    plt.figure()
    plt.bar(df["exercise"], df["max_weight"], color="Red")
    plt.title("Max Weight per Exercise")
    plt.xlabel("Exercise")