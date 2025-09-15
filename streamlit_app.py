import streamlit as st
import pandas as pd
import numpy as np
import datetime

# ---------- LOAD DATA ----------
@st.cache_data
def load_data():
    google = pd.read_csv("google.csv", parse_dates=["date"], dayfirst=True)
    facebook = pd.read_csv("facebook.csv", parse_dates=["date"], dayfirst=True)
    tiktok = pd.read_csv("tiktok.csv", parse_dates=["date"], dayfirst=True)
    business = pd.read_csv("business.csv", parse_dates=["date"], dayfirst=True)

    # Add channel column
    google["channel"] = "google"
    facebook["channel"] = "facebook"
    tiktok["channel"] = "tiktok"

    # Standardize col names
    for df in [google, facebook, tiktok]:
        df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
        df.rename(columns={"impression":"impressions","attributed_revenue":"attributed_revenue"}, inplace=True)

    # Combine
    marketing = pd.concat([google, facebook, tiktok], ignore_index=True)

    # Business cleanup
    business.columns = business.columns.str.strip().str.lower().str.replace(" ", "_")

    return marketing, business

marketing, business = load_data()

# ---------- METRICS ----------
marketing["ctr"] = marketing["clicks"] / marketing["impressions"]
marketing["cpc"] = marketing["spend"] / marketing["clicks"]
marketing["roas"] = marketing["attributed_revenue"] / marketing["spend"]

# ---------- DASHBOARD ----------
st.title("📊 Marketing & Business Performance Dashboard")

# Date filter
date_min = marketing["date"].min().date()
date_max = marketing["date"].max().date()

date_range = st.slider(
    "Select Date Range",
    min_value=date_min,
    max_value=date_max,
    value=(date_min, date_max)
)

# filter data based on date slider
mask = (marketing["date"].dt.date >= date_range[0]) & (marketing["date"].dt.date <= date_range[1])
filtered = marketing.loc[mask]

# KPIs
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Spend", f"${filtered['spend'].sum():,.0f}")
col2.metric("Total Revenue", f"${filtered['attributed_revenue'].sum():,.0f}")
col3.metric("Orders", f"{business['#_of_orders'].sum():,}")
col4.metric("ROAS", f"{filtered['roas'].mean():.2f}x")

# Time series
st.subheader("📈 Spend vs Attributed Revenue Over Time")
daily = filtered.groupby("date").agg({"spend":"sum","attributed_revenue":"sum"}).reset_index()
st.line_chart(daily.set_index("date"))

# Channel performance
st.subheader("📊 Channel Performance")
channel_perf = filtered.groupby("channel").agg({
    "spend":"sum",
    "attributed_revenue":"sum",
    "clicks":"sum",
    "impressions":"sum"
}).reset_index()
channel_perf["roas"] = channel_perf["attributed_revenue"] / channel_perf["spend"]
st.dataframe(channel_perf)

# Campaign leaderboard
st.subheader("🏆 Campaign Leaderboard")
campaign_perf = filtered.groupby("campaign").agg({
    "spend":"sum",
    "attributed_revenue":"sum",
    "clicks":"sum",
    "impressions":"sum"
}).reset_index()
campaign_perf["roas"] = campaign_perf["attributed_revenue"] / campaign_perf["spend"]
st.dataframe(campaign_perf.sort_values("roas", ascending=False))
