import pandas as pd
import matplotlib.pyplot as plt

pd.options.display.max_rows = 9999
df = pd.read_csv('file.csv')

id = input("put the athlete ID? ")

athlete_data = df[df['Athlete ID']==id]

print(athlete_data)