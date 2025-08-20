# analysis.py
# SaaS MRR Growth Analysis for Executive Review
#
# Author: Anand S
# Contact: 23f3000137@ds.study.iitm.ac.in
#
# This script was generated with assistance from an LLM (e.g., ChatGPT Codex).

import pandas as pd
import matplotlib.pyplot as plt

# --- Data Definition ---
# Quarterly MRR Growth data for 2024
data = {
    'Quarter': ['Q1', 'Q2', 'Q3', 'Q4'],
    'MRR Growth': [3.62, 5.79, 9.57, 10.79]
}
df = pd.DataFrame(data)

# --- Analysis ---
# Calculate the average MRR growth
average_growth = df['MRR Growth'].mean()
industry_target = 15

print(f"Dataset successfully processed.")
print(f"Calculated Average MRR Growth: {average_growth:.2f}") # This should output 7.44
print(f"Industry Target: {industry_target}")

# --- Visualization ---
# Create a professional bar chart for the data story
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the quarterly data
bars = ax.bar(df['Quarter'], df['MRR Growth'], color='#4a90e2', label='Quarterly MRR Growth')

# Plot the industry target line for comparison
ax.axhline(y=industry_target, color='#d0021b', linestyle='--', linewidth=2, label=f'Industry Target ({industry_target})')

# Add a line for our calculated average
ax.axhline(y=average_growth, color='#f5a623', linestyle=':', linewidth=2, label=f'2024 Average ({average_growth:.2f})')

# Add labels and titles for clarity
ax.set_title('2024 Quarterly MRR Growth vs. Industry Target', fontsize=16, weight='bold')
ax.set_xlabel('Quarter', fontsize=12)
ax.set_ylabel('MRR Growth (%)', fontsize=12)
ax.set_ylim(0, industry_target + 2) # Set y-axis limit to give space
ax.legend()

# Add data labels on top of the bars
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2.0, yval + 0.2, f'{yval}%', ha='center', va='bottom')

# Save the figure to a file for the README
plt.tight_layout()
plt.savefig('mrr_growth_analysis.png')

print("\nVisualization 'mrr_growth_analysis.png' has been successfully generated.")