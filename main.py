import streamlit as st
from analysis.loader import load_data

df_movies = load_data()

st.title("Netflix Movies Data Overview")

st.subheader("Detailed Data View")
st.dataframe(df_movies)

# Most popular genres
st.subheader("Most Popular Genres")


# Released per Year
st.subheader("Movies Releseased per Year")
