import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Task 1: Load and Explore the Dataset
def load_dataset(file_path):
    try:
        df = pd.read_csv(file_path)
        print("Dataset Loaded Successfully!")
        return df
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"Error loading file: {e}")
    return None

def explore_dataset(df):
    print("\nFirst Five Rows:")
    print(df.head())
    print("\nDataset Info:")
    print(df.info())
    print("\nMissing Values:")
    print(df.isnull().sum())
    df = df.dropna()
    print("\nMissing Values After Cleaning:")
    print(df.isnull().sum())
    return df

# Task 2: Basic Data Analysis
def analyze_data(df):
    print("\nDescriptive Statistics:")
    print(df.describe())
    if 'species' in df.columns:  # Modify for your categorical column
        print("\nMean of Numerical Columns Grouped by Species:")
        print(df.groupby('species').mean())

# Task 3: Data Visualization
def create_visualizations(df):
    plt.figure(figsize=(12, 6))
    
    # Line Chart
    if 'date' in df.columns:  # Modify if dataset has time-series data
        df['date'] = pd.to_datetime(df['date'])
        df.sort_values('date', inplace=True)
        plt.subplot(2, 2, 1)
        plt.plot(df['date'], df.iloc[:, 1])
        plt.title("Trend Over Time")
        plt.xlabel("Date")
        plt.ylabel(df.columns[1])
        plt.xticks(rotation=45)
    
    # Bar Chart
    if 'species' in df.columns:  # Modify for your categorical column
        plt.subplot(2, 2, 2)
        sns.barplot(x='species', y=df.columns[1], data=df)
        plt.title("Category Comparison")
        plt.xticks(rotation=45)
    
    # Histogram
    plt.subplot(2, 2, 3)
    plt.hist(df.iloc[:, 1], bins=20, color='blue', alpha=0.7)
    plt.title("Distribution of Numerical Data")
    plt.xlabel(df.columns[1])
    
    # Scatter Plot
    if df.shape[1] > 2:
        plt.subplot(2, 2, 4)
        sns.scatterplot(x=df.columns[1], y=df.columns[2], data=df)
        plt.title("Relationship Between Two Variables")
    
    plt.tight_layout()
    plt.show()

# Main Execution
dataset_path = "your_dataset.csv"  # Replace with actual dataset path
df = load_dataset(dataset_path)
if df is not None:
    df = explore_dataset(df)
    analyze_data(df)
    create_visualizations(df)
