import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('museum_visitors.csv')

avila_sum = df['Avila Adobe'].sum()
firehouse_sum = df['Firehouse Museum'].sum()
chinese_sum = df['Chinese American Museum'].sum()
america_sum = df['America Tropical Interpretive Center'].sum()

museum_sums = [avila_sum, firehouse_sum, chinese_sum, america_sum]

# Create a bar chart
plt.bar(['Avila Adobe', 'Firehouse Museum', 'Chinese American Museum', 'America Tropical Interpretive Center'], museum_sums)
plt.xlabel("Museum")
plt.xticks(rotation=10)
plt.ylabel("Number of visitors")
plt.title("Number of visitors per museum")

# Show the plot
plt.show()

