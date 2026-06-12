import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------
st.set_page_config(
    page_title="Nifty Valuation Dashboard",
    page_icon="📈",
    layout="wide"
)

# ------------------------------------------------
# LOAD DATA
# ------------------------------------------------
df = pd.read_excel("Till date.xlsx")

# Clean column names
df.columns = df.columns.str.strip()

# Remove unwanted columns
df = df.loc[:, ~df.columns.str.contains("^Unnamed")]

# Remove empty rows
df = df.dropna(subset=["Year"])

# Convert Year to integer
df["Year"] = df["Year"].astype(int)

# Rename misspelled columns
df.rename(columns={
    "10yr Yeild": "10yr Yield",
    "Earning Yeild": "Earning Yield"
}, inplace=True)

# ------------------------------------------------
# SIDEBAR
# ------------------------------------------------
st.sidebar.title("⚙ Filters")

start_year = st.sidebar.slider(
    "Starting Year",
    int(df["Year"].min()),
    int(df["Year"].max()),
    int(df["Year"].min())
)

df = df[df["Year"] >= start_year]

if df.empty:
    st.warning("No data available.")
    st.stop()

latest = df.iloc[-1]

# ------------------------------------------------
# TITLE
# ------------------------------------------------
st.title("📈 Nifty Valuation Dashboard")
st.caption("Historical valuation analysis of the Indian equity market")

# ------------------------------------------------
# KPI CARDS
# ------------------------------------------------
c1, c2, c3, c4 = st.columns(4)

c1.metric("Nifty 50", round(latest["Nifty 50"], 2))
c2.metric("Nifty PE", round(latest["Nifty PE"], 2))
c3.metric("Nifty PB", round(latest["Nifty PB"], 2))
c4.metric("Buffett Indicator", round(latest["Buffett Indicator"], 2))

st.divider()

# ------------------------------------------------
# TABS
# ------------------------------------------------
overview_tab, valuation_tab, returns_tab = st.tabs(
    ["Overview", "Valuation", "Returns"]
)

# =====================================================
# OVERVIEW TAB
# =====================================================
with overview_tab:

    left, right = st.columns(2)

    with left:
        fig1 = px.line(
            df,
            x="Year",
            y="Nifty PE",
            title="Nifty PE Ratio",
            markers=True
        )

        fig1.update_layout(template="plotly_dark", height=450)

        st.plotly_chart(fig1, use_container_width=True)

    with right:
        fig2 = px.line(
            df,
            x="Year",
            y="Nifty PB",
            title="Nifty PB Ratio",
            markers=True
        )

        fig2.update_layout(template="plotly_dark", height=450)

        st.plotly_chart(fig2, use_container_width=True)

    left, right = st.columns(2)

    with left:
        fig3 = px.line(
            df,
            x="Year",
            y="Buffett Indicator",
            title="Buffett Indicator",
            markers=True
        )

        fig3.update_layout(template="plotly_dark", height=450)

        st.plotly_chart(fig3, use_container_width=True)

    with right:
        fig4 = px.histogram(
            df,
            x="Nifty PE",
            title="Distribution of Nifty PE"
        )

        fig4.update_layout(template="plotly_dark", height=450)

        st.plotly_chart(fig4, use_container_width=True)

# =====================================================
# VALUATION TAB
# =====================================================
with valuation_tab:

    left, right = st.columns(2)

    with left:
        fig5 = px.line(
            df,
            x="Year",
            y="BEER ratio",
            title="BEER Ratio",
            markers=True
        )

        fig5.update_layout(template="plotly_dark", height=450)

        st.plotly_chart(fig5, use_container_width=True)

    with right:
        fig6 = px.line(
            df,
            x="Year",
            y="Earning Yield",
            title="Earning Yield",
            markers=True
        )

        fig6.update_layout(template="plotly_dark", height=450)

        st.plotly_chart(fig6, use_container_width=True)

    left, right = st.columns(2)

    with left:
        fig7 = px.line(
            df,
            x="Year",
            y="10yr Yield",
            title="10-Year Yield",
            markers=True
        )

        fig7.update_layout(template="plotly_dark", height=450)

        st.plotly_chart(fig7, use_container_width=True)

    with right:
        fig8 = px.line(
            df,
            x="Year",
            y="Percentile",
            title="Valuation Percentile",
            markers=True
        )

        fig8.update_layout(template="plotly_dark", height=450)

        st.plotly_chart(fig8, use_container_width=True)

    st.subheader("Valuation Score")

    gauge = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=float(latest["Valuation Score"]),
            title={"text": "Valuation Score"},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": "lime"},
                "steps": [
                    {"range": [0, 30], "color": "green"},
                    {"range": [30, 70], "color": "orange"},
                    {"range": [70, 100], "color": "red"}
                ]
            }
        )
    )

    gauge.update_layout(template="plotly_dark", height=500)

    st.plotly_chart(gauge, use_container_width=True)

# =====================================================
# RETURNS TAB
# =====================================================
with returns_tab:

    left, right = st.columns(2)

    with left:
        fig9 = px.scatter(
            df,
            x="Nifty PE",
            y="Future 5yr CAGR",
            trendline="ols",
            title="PE vs Future 5-Year CAGR"
        )

        fig9.update_layout(template="plotly_dark", height=500)

        st.plotly_chart(fig9, use_container_width=True)

    with right:
        fig10 = px.line(
            df,
            x="Year",
            y="Valuation Score",
            title="Valuation Score Trend",
            markers=True
        )

        fig10.update_layout(template="plotly_dark", height=500)

        st.plotly_chart(fig10, use_container_width=True)

# ------------------------------------------------
# SUMMARY TABLE
# ------------------------------------------------
st.divider()

summary = pd.DataFrame({
    "Metric": ["Nifty PE", "Nifty PB", "Buffett Indicator"],
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

st.subheader("Summary Statistics")
st.dataframe(summary, use_container_width=True)
