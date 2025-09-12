import pandas as pd
import matplotlib.pyplot as plt

# Visualizes total volume and max weight per exercise.
def data_visualizer(df: pd.DataFrame):
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    axes[0].bar(df["exercise"], df["total_volume"], color="skyblue")
    axes[0].set_title("Total Volume by Exercise")
    axes[0].set_xlabel("Exercise")
    axes[0].set_ylabel("Total Volume")
    axes[0].tick_params(axis="x", rotation=30)
    axes[1].bar(df["exercise"], df["max_weight"], color="salmon")
    axes[1].set_title("Max Weight by Exercise")
    axes[1].set_xlabel("Exercise")
    axes[1].set_ylabel("Max Weight")
    axes[1].tick_params(axis="x", rotation=30)
    plt.show()
    return fig