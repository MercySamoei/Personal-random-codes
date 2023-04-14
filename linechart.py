import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('museum_visitors.csv')

plt.plot(df['Date'], df['Avila Adobe'], label='Avila Adobe')
plt.plot(df['Date'], df['Firehouse Museum'], label='Firehouse Museum')
plt.plot(df['Date'], df['Chinese American Museum'], label='Chinese American Museum')
plt.plot(df['Date'], df['America Tropical Interpretive Center'], label='America Tropical Interpretive Center')

plt.xlabel('Date')
plt.ylabel('Number of visitors')
plt.xticks(rotation=90)
plt.title('Monthly Visitors to Four Museums')


plt.show()


