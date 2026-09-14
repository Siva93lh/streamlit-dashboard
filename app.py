import streamlit as st
import pandas as pd

# Page settings
st.set_page_config(
    page_title="Sales Dashboard",
    page_icon="📊",
    layout="wide"
)

# Title
st.title("📊 Sales Dashboard")
st.write("Welcome to my first Streamlit dashboard!")

# Sample data
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [12000, 15000, 18000, 14000, 22000, 25000]
}

df = pd.DataFrame(data)

# KPI section
col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", "₹1,06,000")
col2.metric("Average Sales", "₹17,667")
col3.metric("Best Month", "June")

# Chart
st.subheader("Monthly Sales")

st.bar_chart(
    df.set_index("Month")
)

# Data table
st.subheader("Sales Data")

st.dataframe(df)