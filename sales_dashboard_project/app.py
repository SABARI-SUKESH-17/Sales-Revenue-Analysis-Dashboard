
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Sales & Revenue Dashboard", layout="wide")

st.title("📊 Sales & Revenue Analysis Dashboard")

# Load data
df = pd.read_csv("sales_data.csv")

# Sidebar filters
st.sidebar.header("Filters")
product = st.sidebar.multiselect("Select Product", df["Product"].unique(), default=df["Product"].unique())
region = st.sidebar.multiselect("Select Region", df["Region"].unique(), default=df["Region"].unique())

filtered_df = df[(df["Product"].isin(product)) & (df["Region"].isin(region))]

# KPI Metrics
total_sales = filtered_df["Sales"].sum()
total_revenue = filtered_df["Revenue"].sum()

col1, col2 = st.columns(2)

with col1:
    st.metric("Total Sales", f"₹{total_sales:,}")

with col2:
    st.metric("Total Revenue", f"₹{total_revenue:,}")

# Revenue by Product
st.subheader("Revenue by Product")
product_revenue = filtered_df.groupby("Product")["Revenue"].sum()

fig, ax = plt.subplots()
product_revenue.plot(kind="bar", ax=ax)
st.pyplot(fig)

# Sales Trend
st.subheader("Sales Trend")
trend = filtered_df.groupby("Date")["Sales"].sum()

fig2, ax2 = plt.subplots()
trend.plot(ax=ax2)
st.pyplot(fig2)

st.dataframe(filtered_df)
