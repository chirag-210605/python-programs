import pandas as pd 
data={
    'Name':['alice','bob','charlie',None,'eve'],
    'age':[25,None,30,22,None],
    'city':['new york','los angeles',None,'chicago','miami'],
    }
df=pd.DataFrame(data)
def analyze_missing_data(df):
    print("missing data:")
    print(df)
    print("\nMissing data analysis:")
    missing_data=df.isnull().sum()
    print("missing value in each column:")
    print(missing_data[missing_data>0])
    missing_percentage=(missing_data/len(df))*100
    print("\nPrecentage of missing values in each column:")
    print(missing_percentage[missing_percentage>0])
    return missing_data,missing_percentage
def handle_missing_data(df):
    print("\n choose a method to find the missing data:")
    print("1.fill missing values with specified value")
    print("2.drop rows with missing value")
    print("3.drop column with missing values")
    choice=input("enter your choice (1/2/3): ")
    if choice=='1':
        value=input("enter the value to fill missing data: ")
        df_filled=df.fillna(value)
        print("\ndata after filling missing values: ")
        print(df_filled)
    elif choice=='2':
        df_dropped_column=df.dropna()
        print("\ndata after rows with missing values: ")
        print(df_dropped_rows)
    elif choice=='3':
        df_dropped_columns=df.dropna(axis=1)
        print("\ndata after dropping columns with missing values: ")
        print(df_dropped_columns)
    else:
        print("invalid choice!please enter 1,2or 3")
missing_data,missing_percentage=analyze_missing_data(df)
handle_missing_data(df)
