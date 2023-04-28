import pandas as pd
import plotly.express as px

data = pd.read_csv('GDPR.csv') 

grouped = data.groupby(['Country'])['Amount'].sum().reset_index()

sorted_data = grouped.sort_values('Amount', ascending=False).head(10)

fig = px.bar(sorted_data, x='Country', y='Amount', color='Country', 
             title='Top 10 Countries with the Highest Total Violation Amounts')
fig.update_layout(title_x=0.5, showlegend=False)
fig.show()

