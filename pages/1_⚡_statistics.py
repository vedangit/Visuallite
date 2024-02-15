import streamlit as st
import pandas as pd
import plotly.express as px

# Summary Statistics
if st.sidebar.checkbox("Summary Statistics"):
    st.subheader("Summary Statistics")
    summary_stats = df.describe()
    st.write(summary_stats)

# Correlation Analysis
if st.sidebar.checkbox("Correlation Analysis"):
    st.subheader("Correlation Analysis")
    correlation_matrix = df.corr()
    st.write(correlation_matrix)