import streamlit as st
import pandas as pd
from time import sleep

st.title("🎈 My new app")
st.write("Hello")

@st.cache_data
def load_data():
    print("Daten werden geladen")
    # Simulieren, dass CSV größer ist
    df = pd.read_csv("students.csv")
    return df

df = load_data()
st.dataframe(df)

st.slider("Test", 0, 100)

