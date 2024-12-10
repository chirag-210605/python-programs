
import pandas as pd 
import matplotlib.pyplot as plt 
# Sample data: Replace this with actual data reading (e.g., from a CSV file) 
data = { 
'Age': [25, 30, 35, 40, 45, 50, 55, 60, 65, 70], 
'Salary': [20000, 25000, 30000, 35000, 40000, 45000, 50000, 55000, 60000, 
65000], 
'Department': ['HR', 'IT', 'Finance', 'IT', 'Finance', 'HR', 'HR', 'Finance', 'IT', 'Finance'] 
} 
df = pd.DataFrame(data) 
# 1. Scatter Plot of Age vs Salary 
plt.figure(figsize=(8, 5)) 
plt.scatter(df['Age'], df['Salary'], color='blue', marker='o') 
plt.title("Scatter Plot of Age vs Salary") 
plt.xlabel("Age") 
plt.ylabel("Salary") 
plt.grid(True) 
plt.show() 
# 2. Histogram of Age Distribution 
plt.figure(figsize=(8, 5)) 
plt.hist(df['Age'], bins=5, color='green', edgecolor='black') 
plt.title("Histogram of Age Distribution") 
plt.xlabel("Age") 
plt.ylabel("Frequency") 
plt.grid(axis='y') 
plt.show() 
# 3. Bar Plot of Department Counts 
plt.figure(figsize=(8, 5)) 
department_counts = df['Department'].value_counts() 
plt.bar(department_counts.index,department_counts.values,color='orange',edgecolor='black')
plt.title("Bar Plot of Department Counts") 
plt.xlabel("Department") 
plt.ylabel("Number of Employees") 
plt.grid(axis='y') 
plt.show() 
