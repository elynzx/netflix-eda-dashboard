import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    df = pd.read_csv("data/netflix_titles.csv")

    movies = df[df["type"] == "Movie"].copy()
    movies["duration"] = movies["duration"].str.replace(" min", "").astype(float)
    movies = movies.rename(columns={"listed_in": "genre"})
    
    return movies