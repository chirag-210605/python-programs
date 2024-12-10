
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
# Sample data: Replace this with actual data reading (e.g., from a CSV file) 
data = { 
'Department': ['HR', 'IT', 'Finance', 'IT', 'Finance', 'HR', 'HR', 'Finance', 'IT', 'Finance'], 
'Salary': [20000, 25000, 30000, 35000, 40000, 45000, 50000, 55000, 60000, 
65000] 
} 
df = pd.DataFrame(data) 
# Set the Seaborn style for the plot 
sns.set(style="whitegrid") 
# Create a Box and Whisker plot 
plt.figure(figsize=(8, 6)) 
sns.boxplot(data=df, x='Department', y='Salary', palette="Set2") 
# Set titles and labels 
plt.title("Box and Whiskers Plot of Salary by Department") 
plt.xlabel("Department") 
plt.ylabel("Salary") 
plt.show() 
