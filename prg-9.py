
import pandas as pd 
# Sample data: You can replace this with your actual dataset 
data = { 
'Name': ['Alice', 'Bob', 'Charlie', None, 'Eve'], 
'Age': [25, None, 30, 22, None], 
'City': ['New York', 'Los Angeles', None, 'Chicago', 'Miami'], 
} 
# Create a DataFrame 
df = pd.DataFrame(data) 
# Function to analyze missing data 
def analyze_missing_data(df): 
    print("DataFrame:") 
    print(df) 
    print("\nMissing Data Analysis:") 
# Check for missing values 
    missing_data = df.isnull().sum() 
    print("Missing values in each column:") 
    print(missing_data[missing_data > 0]) 
# Calculate percentage of missing values 
    missing_percentage = (missing_data / len(df)) * 100 
    print("\nPercentage of missing values in each column:") 
    print(missing_percentage[missing_percentage > 0]) 
    return missing_data, missing_percentage 
# Function to handle missing data 
def handle_missing_data(df): 
    print("\nChoose a method to handle missing data:") 
    print("1. Fill missing values with a specified value") 
    print("2. Drop rows with missing values") 
    print("3. Drop columns with missing values") 
    choice = input("Enter your choice (1/2/3): ") 
    if choice == '1': 
        value = input("Enter the value to fill missing data: ") 
        df_filled = df.fillna(value) 
        print("\nData after filling missing values:") 
        print(df_filled) 
    elif choice == '2': 
        df_dropped_rows = df.dropna() 
        print("\nData after dropping rows with missing values:") 
        print(df_dropped_rows) 
    elif choice == '3': 
        df_dropped_columns = df.dropna(axis=1) 
        print("\nData after dropping columns with missing values:") 
        print(df_dropped_columns) 
    else: 
        print("Invalid choice! Please enter 1, 2, or 3.") 
# Analyze missing data 
missing_data, missing_percentage = analyze_missing_data(df) 
# Handle missing data 
handle_missing_data(df)
