
 
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
# Sample data: Replace this with actual data reading (e.g., from a CSV file) 
data = { 
'Age': [25, 30, 35, 40, 45, 50, 55, 60, 65, 70], 
'Salary': [20000, 25000, 30000, 35000, 40000, 45000, 50000, 55000, 60000, 
65000], 
'Department': ['HR', 'IT', 'Finance', 'IT', 'Finance', 'HR', 'HR', 'Finance', 'IT', 'Finance'] 
} 
df = pd.DataFrame(data) 
# Set the Seaborn style for all plots 
sns.set(style="whitegrid") 
# 1. Scatter Plot of Age vs Salary 
plt.figure(figsize=(8, 5)) 
sns.scatterplot(data=df, x='Age', y='Salary', hue='Department', palette='viridis', 
s=100) 
plt.title("Scatter Plot of Age vs Salary") 
plt.xlabel("Age") 
plt.ylabel("Salary") 
plt.legend(title='Department') 
plt.show() 
# 2. Histogram of Age Distribution 
plt.figure(figsize=(8, 5)) 
sns.histplot(data=df, x='Age', bins=5, kde=True, color='purple') 
plt.title("Histogram of Age Distribution") 
plt.xlabel("Age") 
plt.ylabel("Frequency") 
plt.show() 
# 3. Bar Plot of Department Counts 
plt.figure(figsize=(8, 5)) 
sns.countplot(data=df, x='Department', palette='pastel') 
plt.title("Bar Plot of Department Counts") 
plt.xlabel("Department") 
plt.ylabel("Number of Employees") 
plt.show() 
