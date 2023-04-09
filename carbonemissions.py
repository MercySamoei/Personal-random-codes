#The average C02 emission per person by food category among five countries (Kenya, Uganda, Tanzania, Rwanda and Ethiopia) located in East Africa.
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Pork': [0.76, 0.02, 0.32, 3.37, 0.29],
    'Chicken': [1.34, 0.66, 1.84, 1.51, 0.47],
    'Beef': [2.53, 3.61, 6.09, 5.15, 9.54],
    'Lamb and Goat': [1.93, 1.57, 1.28, 1.25, 1.86],
    'Fish': [3.88, 0.24, 5.5, 12.5, 4.27],
    'Eggs': [0.16, 0.36, 0.58, 0.97, 1.84],
    'Milk-inc. cheese': [7.23, 44.14, 40.29, 37.27, 94.86],
    'Wheat and wheat products': [11.34, 31.26, 15.94, 10.14, 34.65],
    'Rice': [8.7, 2.25, 0.05, 4.64, 12.94],
    'Soybean': [1.93, 0.45, 0.04, 0.01, 0.2],
    'Nuts inc peanut butter': [0.58, 1.21, 5.94, 3.77, 1.64]
}

df = pd.DataFrame(data, index=['Rwanda', 'Ethiopia', 'Tanzania', 'Uganda', 'Kenya'])

averages = df.mean(axis=0)

print("Average CO2 Emission Per Person by Food Category:")
print(averages)

plt.bar(averages.index, averages.values)
plt.xticks(rotation=90)
plt.ylabel('Average CO2 Emission (kg/person)')
plt.title('Average CO2 Emission Per Person by Food Category')
plt.show()

#Highlight the marked difference between consumption and emissions in certain food product of your choice
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Supplied for consumption (kg/person/year)': [0.16, 0.36, 0.58, 0.97, 1.84],
    'CO2 Emissions (kg/person/year)': [0.15, 0.33, 0.53, 0.89, 1.69]
}

df = pd.DataFrame(data)

df.plot(kind='bar')
plt.xticks(rotation=0)
plt.ylabel('Kilograms')
plt.title('Supplied Amount and CO2 Emissions of Eggs')
plt.legend(loc='upper left')
plt.show()

#The food consumption of animal and non-animal products and the impact on carbon footprint

#Beef's contribution to CO2 emissions (kg/person/year) - Map this.
import matplotlib.pyplot as plt

countries = ['Rwanda', 'Ethiopia', 'Tanzania', 'Uganda', 'Kenya']
emissions = [78.07, 111.4, 187.92, 158.92, 294.38]

plt.bar(countries, emissions)
plt.ylabel('CO2 Emission (kg/person/year)')
plt.title('Beef\'s Contribution to CO2 Emissions in African Countries')
plt.show()

#A box plot and interpretation of the CO2 contributions of food levels.
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'pork': [2.69, 0.07, 1.13, 11.93, 1.03],
    'chicken': [1.44, 0.71, 1.98, 1.62, 0.5],
    'beef': [78.07, 111.4, 187.92, 158.92, 294.38],
    'lamb and goat': [67.59, 54.98, 44.83, 43.77, 65.14],
    'fish': [6.2, 0.38, 8.78, 19.96, 6.82],
    'eggs': [0.15, 0.33, 0.53, 0.89, 1.69],
    'milk-inc. cheese': [10.3, 62.87, 57.39, 53.09, 135.12],
    'Wheat and wheat products': [2.16, 5.96, 3.04, 1.93, 6.61],
    'rice': [11.13, 2.88, 26.89, 5.94, 16.56],
    'soybean': [0.87, 0.2, 0.02, 0, 0.09],
    'nuts inc peanut buter': [1.03, 2.14, 10.51, 6.67, 2.9]
}
df = pd.DataFrame(data)


plt.boxplot(df.values, labels=df.columns)
plt.ylabel('CO2 emissions (kg/person/year)')
plt.xticks(rotation=90)
plt.title('CO2 contributions of food levels')
plt.show()

#Top 10 Countries with highest emissions. Choose the appropriate visual type. Get inspiration from this image
import matplotlib.pyplot as plt

countries = ['Argentina', 'Australia', 'Albania', 'Iceland', 'New Zealand', 'USA', 'Uruguay', 'Luxembourg', 'Brazil', 'Kazakhstan']
emissions = [2108.9, 1852.46, 1689.62, 1679.75, 1668.67, 1642.72, 1560.41, 1544.97, 1508.65, 1502.91]

plt.barh(countries, emissions, color='blue')

plt.xlabel('Emissions (metric tons CO2 equivalent)')
plt.ylabel('Country')
plt.title('Top 10 Countries with highest emissions')

plt.show()

