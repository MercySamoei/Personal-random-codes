import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

data = pd.read_csv('museum_visitors.csv', index_col='Date', parse_dates=True)

totals = []
for month in range(1, 13):
    total = data.loc[(data.index.month == month), ['Avila Adobe', 'Firehouse Museum', 'Chinese American Museum', 'America Tropical Interpretive Center']].sum().sum()
    totals.append(total)

plt.bar([datetime(2000, month, 1).strftime('%B') for month in range(1, 13)], totals)
plt.xlabel("Month")
plt.xticks(rotation=90)
plt.ylabel("Number of visitors")
plt.title("Number of visitors to all the museums")
plt.show()

