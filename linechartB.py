import pandas as pd
import matplotlib.pyplot as plt
#import seaborn as sns

data = pd.read_csv('GDPR.csv')
data['Date'] = data['Date'].astype(str) # convert 'Date' column to string
plt.bar(data['Date'], data['Type'])
plt.xticks(rotation=90)
#plt.yticks(rotation=90)
plt.show()
# Create a pandas DataFrame from the data





