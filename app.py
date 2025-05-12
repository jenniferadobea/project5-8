
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="World Happiness Dashboard", layout="wide")
st.title("Interactive World Happiness Data Dashboard")

# File uploader
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("🔍 Data Preview")
    st.dataframe(df.head())

    st.subheader("📊 Summary Statistics")
    st.dataframe(df.describe())

    st.subheader("🔎 Filter Data")
    filter_column = st.selectbox("Filter by column:", df.columns)
    filter_value = st.selectbox("Choose value:", df[filter_column].dropna().unique())
    filtered_df = df[df[filter_column] == filter_value]
    st.write(f"Filtered data for {filter_column} = {filter_value}:")
    st.dataframe(filtered_df)

    st.subheader("📈 Data Visualization")
    x_column = st.selectbox("X-axis:", df.columns, key="x")
    y_column = st.selectbox("Y-axis:", df.columns, key="y")

    if st.button("Generate Line Chart"):
        try:
            chart_data = filtered_df[[x_column, y_column]].dropna()
            chart_data = chart_data.sort_values(by=x_column)
            st.line_chart(chart_data.set_index(x_column))
        except Exception as e:
            st.error(f"Could not generate chart: {e}")

    if st.button("Generate Bar Chart"):
        try:
            chart_data = filtered_df[[x_column, y_column]].dropna()
            st.bar_chart(chart_data.set_index(x_column))
        except Exception as e:
            st.error(f"Could not generate chart: {e}")

    if st.button("Generate Scatter Plot"):
        try:
            fig, ax = plt.subplots()
            ax.scatter(filtered_df[x_column], filtered_df[y_column])
            ax.set_xlabel(x_column)
            ax.set_ylabel(y_column)
            st.pyplot(fig)
        except Exception as e:
            st.error(f"Could not generate chart: {e}")
else:
    st.info("Please upload a CSV file to begin.")
