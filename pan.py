#import pandas as pd

#df=pd.read_csv('spotify.csv')

#print(df)
import pandas as pd
df = pd.read_csv('spotify.csv')
df_sorted = df.sort_values('Shape of You', ascending=False)
df_sorted = df.sort_values('Despacito', ascending=False)
df_sorted = df.sort_values('Something Just Like This', ascending=False)
df_sorted = df.sort_values('HUMBLE.', ascending=False)
df_sorted = df.sort_values('Unforgettable', ascending=False)
print(df_sorted.head(5))



import pandas as pd

df = pd.read_csv('spotify.csv')

# Group the DataFrame by the 'song' column and get the max 'total days' for each group
most_streamed_days = df.groupby('Despacito').max()

# Print the result
print(most_streamed_days)



