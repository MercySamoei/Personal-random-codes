import pandas as pd
import matplotlib as plt
import seaborn as sbn

df = pd.read_csv('museum_visitors.csv')
#print(df.corr()) to print the correlation between the values
#print(df) to print all the values
#print(df.duplicated()) to check for duplicates

df.plot(kind = 'scatter', x = 'America Tropical Interpretive Center', y = 'Chinese American Museum')

plt.show()


