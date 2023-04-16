import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

dp = pd.read_csv('museum_visitors.csv')
dp['Date'] = pd.to_datetime(dp['Date'])
columns = ['Date', 'Avila Adobe', 'Firehouse Museum', 'Chinese American Museum', 'America Tropical Interpretive Center']
df = dp[columns]
res = df.groupby(df.Date.dt.to_period("Y")).sum()

# create a bar chart
ax = res.plot(kind='bar')
ax.set_xticklabels(res.index.strftime('%Y'))
ax.set_xlabel('Year')
ax.set_ylabel('Number of Visitors')
ax.set_title('Number of Visitors per Year to a Museum')
plt.show()
