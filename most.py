import pandas as pd
import matplotlib.pyplot as plt

# read in the data
df = pd.read_csv('museum_visitors.csv')

# loop through each museum
for museum in ['Avila Adobe', 'Firehouse Museum', 'Chinese American Museum', 'America Tropical Interpretive Center']:
    
    # group the data by date and sum the visitors for the current museum
    grouped = df.groupby('Date')[museum].sum()
    
    top_5 = grouped.sort_values(ascending=False)[:5]
    
    # plot a bar chart for the top 5 days
    plt.bar(top_5.index, top_5.values)
    plt.xticks(rotation=90)
    plt.ylabel('Number of visitors')
    plt.title(f"Top 5 days when '{museum}' had the most visitors")
    
    # show the plot
    plt.show()

