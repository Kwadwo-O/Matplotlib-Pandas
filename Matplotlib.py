import pandas as pd
import matplotlib.pyplot as plt
#
# pd.options.display.max_rows = 9999
# df = pd.read_csv('file.csv')
#
# # id = input("put the athlete ID\n ")
# # athlete_data = df[df['Athlete ID']==id]
#
# sport = input("put the sport - ")
#
# data = input("what data do you want to see? - ")
#
# xpoints = df[df['Sport'] == sport][sport]
# ypoints = df[df['Sport'] == sport][data]
#
# print(xpoints,"\n",ypoints)
#
# plt.bar(xpoints,ypoints, color='#2E75B6')
# plt.title(f'{data} for {sport} Athletes', fontweight='bold')
#
# plt.xlabel('Athlete ID')
# plt.ylabel(data)
#
# plt.show()


# df = pd.read_csv('file.csv')
#
# data = input("What data do you want to compare? ")
#
# avg = df.groupby('Sport')[data].mean()
#
# plt.bar(avg.index, avg.values, color='#2E75B6')
# plt.title(f'Average {data} by Sport', fontweight='bold')
# plt.xlabel('Sport')
# plt.ylabel(f'Average {data}')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()