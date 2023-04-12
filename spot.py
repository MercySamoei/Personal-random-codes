
import pandas as pd

# Load the data
df = pd.read_csv('spotify.csv')

# Group the data by the 'Song Name' column and get the max 'Streams' for each group
most_streamed_days = df.groupby('Song Name')['Streams'].max()

# Print the result
print(most_streamed_days.head(5))
