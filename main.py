import streamlit as st
import pandas as pd
import plotly.express as px

# Set page title and favicon
st.set_page_config(
    page_title="Visuallite - A data visualization tool",
    page_icon=":chart_with_upwards_trend:"
)

# Set title and sidebar header
st.title("Visuallite - A data visualization tool")
st.sidebar.header("Visual picker")

# Set background color and text color
st.markdown(
    """
    <style>
    .reportview-container {
        background: #f8f9fa;
        color: #1e1e1e;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Set font and padding for sidebar
st.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        font-family: Arial, sans-serif;
        padding: 1rem;
        
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Upload CSV file and display DataFrame
st.subheader("Uploaded Dataset:")
uploaded_file = st.sidebar.file_uploader(label="Upload your CSV file", type=['csv'])
df = pd.DataFrame([1, 2, 3])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)

# Select chart type and features
select_chart = st.sidebar.selectbox(
    label="Select Chart Type",
    options=['None', 'Line Plots', 'Scatter Plots', 'Histogram Plots', 'Bar Plots', 'Box Plots', 'Violin Plots']
)
columns_list = df.columns.tolist()

if select_chart != 'None':
    st.sidebar.subheader(select_chart + " Features")
    select_x = st.sidebar.selectbox('X axis', options=columns_list)
    select_y = st.sidebar.selectbox('Y axis', options=columns_list)
    variation = st.sidebar.selectbox('Color Variation', options=columns_list)
    
    if select_chart == 'Line Plots':
        plot = px.line(df, x=select_x, y=select_y, color=variation)
    elif select_chart == 'Scatter Plots':
        plot = px.scatter(df, x=select_x, y=select_y, color=variation)
    elif select_chart == 'Histogram Plots':
        plot = px.histogram(df, x=select_x, y=select_y, color=variation)
    elif select_chart == 'Bar Plots':
        plot = px.bar(df, x=select_x, y=select_y, color=variation)
    elif select_chart == 'Box Plots':
        plot = px.box(df, x=select_x, y=select_y, color=variation)
    elif select_chart == 'Violin Plots':
        plot = px.violin(df, x=select_x, y=select_y, color=variation)

    st.plotly_chart(plot)
