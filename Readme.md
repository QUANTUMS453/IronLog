# ⚒️ IronLog

*A personal workout tracker & analyzer powered by Pandas + Numpy*

## 📖 Overview

**IronLog** is a Python project for tracking and analyzing weightlifting progress.
It takes a simple CSV of workouts (exercise, sets, reps, weight) and turns it into meaningful stats and insights.
The goal: combine **data analysis** with **real gym progress**.

---

## ✨ Features (planned & implemented)

* [x] Load and clean workout logs from CSV
* [x] Normalize dates and exercise names
* [x] Calculate workout volume (sets × reps × weight)
* [x] Session summaries (daily totals, averages, intensity)
* [ ] Track progress over time per exercise
* [ ] Highlight personal records (PRs)
* [ ] Exercise distribution analysis (push/pull/legs split)
* [ ] Weekly/monthly trends
* [ ] Visualization (progress graphs, distributions, trends)

--- 

## 📂 Project Structure

```
IronLog/
│
├── data/
│   └── Workout_Data.csv       # raw workout logs
│
├── ironlog/
│   ├── __init__.py            # package marker
│   ├── loader.py              # load & clean data
│   ├── analyzer.py            # analysis functions
│   ├── visualizer.py          # plots & charts
│   └── utils.py               # helper functions
│
├── main.py                    # entry point
├── requirements.txt           # dependencies
└── README.md                  # this file
```

---

## 🚀 Usage

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the project

```bash
python main.py
```

## 🛠️ Tech Stack

* **Python 3.x**
* [Pandas](https://pandas.pydata.org/) — data handling
* [Numpy](https://numpy.org/) — vectorized analysis
* [Matplotlib](https://matplotlib.org/) — visualizations (planned)

---

## 🎯 Goals

IronLog is a **learning-by-building project**.

* Build better coding structure (modules, packages, testing).
* Practice data analysis with real gym data.
* Create a personal tool that actually helps in training.
* Run on a website
* Learn API

---

## 📌 Status

🚧 Work in progress. Currently working on the analyzer module.
