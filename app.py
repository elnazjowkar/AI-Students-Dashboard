import streamlit as st
import pandas as pd

df = pd.read_csv("AI_Impact_Student_Life_2026.csv")

st.title("AI Student Dashboard")

st.write(df.head())