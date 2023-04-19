import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('GDPR.csv')

# Melt the DataFrame to create a "long" format suitable for plotting
df_melted = data.melt(id_vars=['Date'], var_name='Type')


# Create the line chart using seaborn
sns.set_style('darkgrid')
sns.lineplot(x='Date', y='Type', data=df_melted)

# Add title and axis labels
plt.title('Line Chart of timebreakdown of violations')
plt.xlabel('Date')
plt.ylabel('Value')

# Show the chart
plt.show()