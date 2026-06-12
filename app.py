import streamlit as st
import pandas as pd
import plotly.express as px

# Load Excel file
df = pd.read_excel("Till date.xlsx")

st.title("Nifty Valuation Dashboard")

# Show data
st.subheader("Dataset")
st.dataframe(df)

# Select a column to plot
column = st.selectbox(
    "Choose a column",
    df.columns[1:]
)

# Create chart
fig = px.line(df, x=df.columns[0], y=column)

st.plotly_chart(fig)
