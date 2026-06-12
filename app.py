import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(
    page_title="Nifty Valuation Dashboard",
    page_icon="📈",
    layout="wide"
)

# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------
df = pd.read_excel("Till date.xlsx")

# Rename first column to Year if needed
df.rename(columns={df.columns[0]: "Year"}, inplace=True)

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------
st.sidebar.header("Filters")

start_year = st.sidebar.slider(
    "Select Starting Year",
    int(df["Year"].min()),
    int(df["Year"].max()),
    int(df["Year"].min())
)

df = df[df["Year"] >= start_year]

# Latest values
latest = df.iloc[-1]

# ---------------------------------------------------
# TITLE
# ---------------------------------------------------
st.title("📈 Nifty Valuation Dashboard")
st.markdown("---")

# ---------------------------------------------------
# KPI CARDS
# ---------------------------------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Nifty 50",
    round(latest["Nifty 50"], 2)
)

col2.metric(
    "Nifty PE",
    round(latest["Nifty PE"], 2)
)

col3.metric(
    "Nifty PB",
    round(latest["Nifty PB"], 2)
)

col4.metric(
    "Buffett Indicator",
    round(latest["Buffett Indicator"], 2)
)

st.markdown("---")

# ---------------------------------------------------
# CHART ROW 1
# ---------------------------------------------------
left, right = st.columns(2)

with left:
    fig1 = px.line(
        df,
        x="Year",
        y="Nifty PE",
        title="Nifty PE Ratio",
        markers=True
    )

    fig1.update_layout(
        template="plotly_dark",
        height=450
    )

    st.plotly_chart(fig1, use_container_width=True)

with right:
    fig2 = px.line(
        df,
        x="Year",
        y="Nifty PB",
        title="Nifty PB Ratio",
        markers=True
    )

    fig2.update_layout(
        template="plotly_dark",
        height=450
    )

    st.plotly_chart(fig2, use_container_width=True)

# ---------------------------------------------------
# CHART ROW 2
# ---------------------------------------------------
left, right = st.columns(2)

with left:
    fig3 = px.line(
        df,
        x="Year",
        y="Buffett Indicator",
        title="Buffett Indicator",
        markers=True
    )

    fig3.update_layout(
        template="plotly_dark",
        height=450
    )

    st.plotly_chart(fig3, use_container_width=True)

with right:
    fig4 = px.histogram(
        df,
        x="Nifty PE",
        title="Distribution of Nifty PE"
    )

    fig4.update_layout(
        template="plotly_dark",
        height=450
    )

    st.plotly_chart(fig4, use_container_width=True)

# ---------------------------------------------------
# CHART ROW 3
# ---------------------------------------------------
left, right = st.columns(2)

with left:
    fig5 = px.scatter(
        df,
        x="Nifty PE",
        y="Future 5yr CAGR",
        trendline="ols",
        title="PE vs Future 5-Year CAGR"
    )

    fig5.update_layout(
        template="plotly_dark",
        height=450
    )

    st.plotly_chart(fig5, use_container_width=True)

with right:
    fig6 = px.line(
        df,
        x="Year",
        y="Valuation Score",
        title="Valuation Score",
        markers=True
    )

    fig6.update_layout(
        template="plotly_dark",
        height=450
    )

    st.plotly_chart(fig6, use_container_width=True)

# ---------------------------------------------------
# SUMMARY TABLE
# ---------------------------------------------------
st.markdown("---")
st.subheader("Summary Statistics")

summary = pd.DataFrame({
    "Metric": [
        "Nifty PE",
        "Nifty PB",
        "Buffett Indicator"
    ],
    "Current": [
        latest["Nifty PE"],
        latest["Nifty PB"],
        latest["Buffett Indicator"]
    ],
    "Average": [
        df["Nifty PE"].mean(),
        df["Nifty PB"].mean(),
        df["Buffett Indicator"].mean()
    ],
    "Minimum": [
        df["Nifty PE"].min(),
        df["Nifty PB"].min(),
        df["Buffett Indicator"].min()
    ],
    "Maximum": [
        df["Nifty PE"].max(),
        df["Nifty PB"].max(),
        df["Buffett Indicator"].max()
    ]
})

st.dataframe(summary, use_container_width=True)
