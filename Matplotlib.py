import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('file.csv')

issue = input("put the athlete ID? ")

issue_counts = df[df['Athlete ID']==issue]

plt.bar(issue_counts.index, issue_counts.values, color='#2E75B6')
plt.title('Number of Issues by Type', fontweight='bold')
plt.xlabel('Issue Type')
plt.ylabel('Count')
plt.xticks(rotation=15)


plt.tight_layout()
plt.show()