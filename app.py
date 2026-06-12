import streamlit as st
import pandas as pd
import plotly.express as px

# Page settings
st.set_page_config(
    page_title="Nifty Valuation Dashboard",
    layout="wide"
)

# Load data
df = pd.read_excel("Till date.xlsx")

# Dashboard title
st.title("📈 Nifty Valuation Dashboard")

# Latest values
latest = df.iloc[-1]

col1,col2,col3,col4 = st.columns(4)

col1.metric("Nifty 50", round(latest["Nifty 50"],2))
col2.metric("Nifty PE", round(latest["Nifty PE"],2))
col3.metric("Nifty PB", round(latest["Nifty PB"],2))
col4.metric("10yr Yield", round(latest["10yr Yield"],4))

# Charts
left,right = st.columns(2)

fig1 = px.line(
    df,
    x="Year",
    y="Nifty PE",
    title="Nifty PE Ratio"
)

fig2 = px.line(
    df,
    x="Year",
    y="Nifty PB",
    title="Nifty PB Ratio"
)

with left:
    st.plotly_chart(fig1,use_container_width=True)

with right:
    st.plotly_chart(fig2,use_container_width=True)
