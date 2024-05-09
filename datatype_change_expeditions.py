import pandas as pd

data = pd.read_csv('expeditions_data.csv')

data['bcdate'] = pd.to_datetime(data['bcdate'], errors='coerce', format='%d/%m/%Y')
data['smtdate'] = pd.to_datetime(data['smtdate'], errors='coerce', format='%d/%m/%Y')
data['termdate'] = pd.to_datetime(data['termdate'], errors='coerce', format='%d/%m/%Y')

print(data[['bcdate', 'smtdate', 'termdate']].head())
print(data['bcdate'].isna().sum())
print(data['smtdate'].isna().sum())
print(data['termdate'].isna().sum())
print(data[data['termdate'].isna()][['bcdate', 'smtdate', 'termdate']])


data['nation'] = data['nation'].astype('category')
data['approach'] = data['approach'].astype('category')
data['route1'] = data['route1'].astype('category')
data['route2'] = data['route2'].astype('category')
data['route3'] = data['route3'].astype('category')
