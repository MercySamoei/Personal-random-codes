
import pandas as pd
import random

df = pd.read_csv('Book1.csv', encoding='ISO-8859-1')
print(df)

new_df = df.fillna(value=float('NaN'))
df.fillna(value=random.random(), inplace=True)
new_df.fillna(value=random.random(), inplace=True)

print(new_df.to_string())
print(new_df)

