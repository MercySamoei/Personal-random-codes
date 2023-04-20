import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a pandas DataFrame from the data
data = {'Year': ['2012', '2014'],
        'Mean': [1.9, 1.7],
        'STD': [1, 1.2],
        '50%': [0.7, 0.6],
        '25%': [0.5, 0.8],
        'MAX': [0.747, 0.33],
        'MIN': [0.44, 0.66]}
df = pd.DataFrame(data)

# Melt the DataFrame to create a "long" format suitable for plotting
df_melted = df.melt(id_vars=['Year'], var_name='Stat')

# Create the line chart using seaborn
sns.set_style('darkgrid')
sns.lineplot(x='Year', y='value', hue='Stat', data=df_melted)

# Add title and axis labels
plt.title('Line Chart of Statistical Measures')
plt.xlabel('Year')
plt.ylabel('Value')

# Show the chart
plt.show()
