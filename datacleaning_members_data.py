import pandas as pd

data = pd.read_csv('expeditions_data.csv')
print(data.head())
print(data.info()) #this is an important step for me to
#chek that each column hs the correct data type
print(data.describe())

#above I am just loading the data with pandas and performing
#intial inspections to make sure everything is in order

