# import pandas as pd

# # Load the dataset
# tdf_winners = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-04-07/tdf_winners.csv')

# # Check for missing values
# print(tdf_winners.isnull().sum())

# # Check for duplicates
# print(tdf_winners.duplicated().sum())

# # Check for data types
# print(tdf_winners.dtypes)

# # Check for outliers
# print(tdf_winners['winning_time'].describe())
import urllib.request
import pandas as pd

url = 'https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-04-07/tdf_winners.csv'
filename = 'tdf_winners.csv'

urllib.request.urlretrieve(url, filename)
tdf_winners = pd.read_csv(filename)
