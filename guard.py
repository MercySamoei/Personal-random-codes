import pandas as pd

# Load the dataset from the link
url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/Students_Alcohol_Consumption/student-mat.csv'
df = pd.read_csv(url, delimiter=';')

# Slice the dataframe from school until the guardian column
df = df.loc[:, 'school':'guardian']
print(df.head())
