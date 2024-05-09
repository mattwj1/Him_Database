import pandas as pd

data = pd.read_csv('expeditions_data.csv')
print(data.head())
print(data.info())
print(data.describe())

#above I am just loading the data with pandas and performing
#intial inspections to make sure everything is in order