import pandas as pd
import streamlit as st
import os

@st.cache_data
def load_data():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(BASE_DIR, "data", "seller_6m.csv")

    df = pd.read_csv(csv_path)
    return df