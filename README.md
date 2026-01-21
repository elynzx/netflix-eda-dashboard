# Netflix EDA Dashboard

This project is an interactive dashboard for exploratory data analysis (EDA) of Netflix movies, built with Python and Streamlit.
It allows users to explore, visualize, and analyze the Netflix titles dataset in a simple and dynamic way.

## Features

- Load and filter movie data from a CSV file
- Interactive table visualization
- Analysis of most popular genres
- Movie count by release year
- Simple metrics such as:
  - Longest and shortest movies
  - Top directors
  - Rating-based trends

## Project Structure
```
├── analysis
│   ├── __init__.py
│   ├── charts.py
│   ├── loader.py
│   └── metrics.py
├── data
│   └── netflix_titles.csv
├── .gitignore
├── README.md
├── main.py
└── requirements.txt
```

## Installation

1. Clone the repository and navigate to the project folder.

2. Install the dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
streamlit run main.py
```

### Dataset

The file `data/netflix_titles.csv` contains information about Netflix titles.
For this project, the dataset is filtered to include movies only.

## Purpose

This project was created as a learning exercise to practice:
- Python data analysis with pandas
- Basic project organization
- Interactive dashboards using Streamlit

It is intended as a first EDA project and a foundation for future improvements.

## Acknowledgments

This project was inspired by data analysis concepts learned from DataCamp, and developed independently as hands-on practice.
