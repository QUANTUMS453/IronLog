from fastapi import FastAPI
from fastapi.responses import FileResponse
from pathlib import Path
import pandas as pd

from .loader import load_data, clean_data
from .analyzer import summarize
from .visualizer import data_visualizer

# Create a FastAPI app instance
app = FastAPI(
    title="IronLog API",
    description="An API for tracking and analyzing weightlifting progress.",
    version="1.0.0"
)

# Define the path to the workout data
DATA_PATH = Path(__file__).parent.parent / "Data" / "Workout_Data2.csv"

@app.on_event("startup")
def load_and_clean_data():
    """Load and clean data at application startup to be reused across endpoints."""
    global df
    raw_df = load_data(DATA_PATH)
    df = clean_data(raw_df)
    print("Data loaded and cleaned successfully.")

@app.get("/")
def read_root():
    """A root endpoint to confirm the API is running."""
    return {"message": "Welcome to the IronLog API!"}

@app.get("/data", summary="Get Cleaned Workout Data")
def get_data():
    """Returns the entire cleaned workout dataset as JSON."""
    return df.to_dict(orient="records")

@app.get("/summary/{by}", summary="Get Workout Summaries")
def get_summary(by: str):
    """
    Returns a workout summary grouped by 'date' or 'exercise'.
    """
    if by not in ["date", "exercise"]:
        return {"error": "Invalid grouping. Choose 'date' or 'exercise'."}
    
    summary_df = summarize(df, by=by)
    return summary_df.to_dict(orient="records")

@app.get("/visualization/exercise_summary", summary="Get Exercise Summary Visualization")
def get_exercise_visualization():
    """
    Generates and returns a PNG image of the exercise summary.
    """
    excercise_summary = summarize(df, by="exercise")
    fig = data_visualizer(excercise_summary)
    
    # Save the plot to a temporary file
    image_path = Path("exercise_summary.png")
    fig.savefig(image_path)
    
    return FileResponse(image_path, media_type="image/png")