
import pandas as pd 
import numpy as np 
from scipy.stats import pearsonr 
# Sample data: You can replace this with any dataset you read from a file or create 
data = { 
'Variable_A': [1, 2, 3, 4, 5, 6], 
'Variable_B': [2, 3, 4, 5, 6, 7] 
} 
df = pd.DataFrame(data) 
# 1. Calculate Correlation 
def calculate_correlation(df, col1, col2): 
    correlation, _ = pearsonr(df[col1], df[col2]) 
    return correlation 
# 2. Calculate Joint Probability (P(A and B)) 
def joint_probability(df, event_A, event_B): 
    joint_df = df[(df['Variable_A'] == event_A) & (df['Variable_B'] == event_B)] 
    joint_prob = len(joint_df) / len(df) 
    return joint_prob 
# 3. Calculate Marginal Probability (P(A) or P(B)) 
def marginal_probability(df, event, variable): 
    marginal_df = df[df[variable] == event] 
    marginal_prob = len(marginal_df) / len(df) 
    return marginal_prob 
# 4. Calculate Conditional Probability (P(A|B) = P(A and B) / P(B)) 
def conditional_probability(df, event_A, event_B): 
    joint_prob = joint_probability(df, event_A, event_B) 
    marginal_prob_B = marginal_probability(df, event_B, 'Variable_B') 
    if marginal_prob_B == 0: 
        return 0  # Avoid division by zero 
    return joint_prob / marginal_prob_B 
# Example Usage 
# Correlation between Variable_A and Variable_B 
correlation = calculate_correlation(df, 'Variable_A', 'Variable_B') 
print("Correlation between Variable_A and Variable_B:", correlation) 
# Joint Probability P(A=3 and B=4) 
joint_prob = joint_probability(df, 3, 4) 
print("Joint Probability P(A=3 and B=4):", joint_prob) 
# Marginal Probability P(A=3) 
marginal_prob_A = marginal_probability(df, 3, 'Variable_A') 
print("Marginal Probability P(A=3):", marginal_prob_A) 
# Marginal Probability P(B=4) 
marginal_prob_B = marginal_probability(df, 4, 'Variable_B') 
print("Marginal Probability P(B=4):", marginal_prob_B) 
# Conditional Probability P(A=3 | B=4) 
cond_prob = conditional_probability(df, 3, 4) 
print("Conditional Probability P(A=3 | B=4):", cond_prob) 
