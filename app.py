import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Hyperliquid Trader Sentiment Dashboard")

data = pd.read_csv("processed_data.csv")

sentiment_choice = st.selectbox(
    "Select Sentiment",
    data['classification'].unique()
)

filtered = data[data['classification']==sentiment_choice]

st.write(filtered.describe())

fig, ax = plt.subplots()
ax.hist(filtered['daily_pnl'], bins=30)
st.pyplot(fig)
