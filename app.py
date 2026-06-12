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

# KPI cards
col1,col2,col3,col4 = st.columns(4)

col1.metric("Nifty 50", round(latest["Nifty 50"],2))
col2.metric("Nifty PE", round(latest["Nifty PE"],2))
col3.metric("Nifty PB", round(latest["Nifty PB"],2))
col4.metric("Buffett Indicator", round(latest["Buffett Indicator"],2))

# Charts row 1
left,right = st.columns(2)

with left:
    fig1 = px.line(
        df,
        x=df.columns[0],
        y="Nifty PE",
        title="Nifty PE Ratio"
    )
    st.plotly_chart(fig1,use_container_width=True)

with right:
    fig2 = px.line(
        df,
        x=df.columns[0],
        y="Nifty PB",
        title="Nifty PB Ratio"
    )
    st.plotly_chart(fig2,use_container_width=True)

# Charts row 2
left,right = st.columns(2)

with left:
    fig3 = px.line(
        df,
        x=df.columns[0],
        y="Buffett Indicator",
        title="Buffett Indicator"
    )
    st.plotly_chart(fig3,use_container_width=True)

with right:
    fig4 = px.histogram(
        df,
        x="Nifty PE",
        title="Distribution of Nifty PE"
    )
    st.plotly_chart(fig4,use_container_width=True)


