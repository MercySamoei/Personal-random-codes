import pandas as pd

# Read in the dataset
df = pd.read_csv("https://raw.githubusercontent.com/datasets/investor-flow-of-funds-us/master/data/weekly.csv")

# Convert the 'Date' column to a datetime datatype
df['Date'] = pd.to_datetime(df['Date'])

# Set the 'Date' column as the index
df.set_index('Date', inplace=True)

# Print the data type of the index
print(df.index.dtype)


