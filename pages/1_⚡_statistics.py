import streamlit as st
import pandas as pd
from main import df  #import the dataframe from main
import plotly.express as px


#statistical summary
if st.sidebar.checkbox("Summary Statistics"):
    st.subheader("Summary Statistics")
    summary_stats = st.session_state.df.describe()
    st.write(summary_stats)

#correlation analysis
if st.sidebar.checkbox("Correlation Analysis"):
    st.subheader("Correlation Analysis")
    correlation_matrix = st.session_state.df.corr()
    st.write(correlation_matrix)

#function to detect outliers
def detect_outliers(data, threshold=1.5):
    #find IQR
    q1 = data.quantile(0.25)
    q3 = data.quantile(0.75)
    iqr = q3 - q1
    
    #lower bound anf upper bound
    lower_bound = q1 - threshold * iqr
    upper_bound = q3 + threshold * iqr
    return (data < lower_bound) | (data > upper_bound)

#outlier analysis
if st.sidebar.checkbox("Outlier Analysis"):
    st.subheader("Outlier Analysis")

    selected_column = st.sidebar.selectbox("Select a column for outlier detection", options=df.columns)

    #threshold from 0-3
    threshold = st.sidebar.slider("Outlier Threshold", min_value=0.1, max_value=3.0, step=0.1, value=1.5)

    #detecting outliers
    outliers = detect_outliers(df[selected_column], threshold=threshold)

    #return the count
    num_outliers = outliers.sum()
    st.write(f"Number of outliers in {selected_column}: {num_outliers}")


    #return dataframe made of outliers
    if num_outliers > 0:
        st.write("Outliers:")
        st.write(df[outliers])

    #box plot of outliers (?not sure if its the most optimal)
    # box_plot = px.box(df, y=selected_column, points="all")
    # box_plot.update_traces(marker=dict(color='red', size=5), selector=dict(mode='markers', marker_color='red'))
    # st.plotly_chart(box_plot)
    
    #shifting to scatterplot
    
# Create scatter plot with outliers highlighted
scatter_plot = px.scatter(df, x=df.index, y=selected_column, title=f"{selected_column} Outliers")

# Update marker properties for outliers
scatter_plot.update_traces(marker=dict(color='red', size=5), selector=dict(mode='markers', marker_color='red'))

# Display the scatter plot
st.plotly_chart(scatter_plot)
