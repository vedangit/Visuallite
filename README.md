# Visuallite - A Data Visualization Tool

Visuallite is a web-based data visualization tool built with Streamlit. It allows users to upload CSV files, explore summary statistics, analyze correlations, detect outliers, and visualize data using various chart types.

## Features

- [x] **Upload CSV File**: Users can upload their own CSV files to analyze and visualize their data.
- [x] **Summary Statistics**: Explore summary statistics including mean, median, standard deviation, minimum, maximum, etc.
- [x] **Correlation Analysis**: Analyze correlations between different variables in the dataset.
- [x] **Outlier Detection**: Detect outliers in the data using the interquartile range (IQR) method and visualize them on scatter plots.
- [x] **Interactive Chart Selection**: Choose from various chart types including line plots, scatter plots, histograms, bar plots, box plots, and violin plots.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/visuallite.git
    ```

2. Navigate to the project directory:

    ```bash
    cd visuallite
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the Streamlit app:

    ```bash
    streamlit run main.py
    ```

## Usage

1. **Upload CSV file**: Use the sidebar file uploader to upload your CSV file.
2. **Explore Summary Statistics and Correlation Analysis**: Select the respective checkboxes in the sidebar to explore summary statistics and analyze correlations.
3. **Outlier Analysis**: Enable the outlier analysis checkbox in the sidebar to detect outliers in the data and visualize them on scatter plots.
4. **Visualize Data**: Choose from various chart types available in the sidebar to visualize your data interactively.



