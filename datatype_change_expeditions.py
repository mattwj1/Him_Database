import pandas as pd

data = pd.read_csv('expeditions_data.csv')

data['bcdate'] = pd.to_datetime(data['bcdate'], errors='coerce', format='%d/%m/%Y')
data['smtdate'] = pd.to_datetime(data['smtdate'], errors='coerce', format='%d/%m/%Y')
data['termdate'] = pd.to_datetime(data['termdate'], errors='coerce', format='%d/%m/%Y')

data.dropna(subset=['bcdate', 'smtdate'], inplace=True)

data['nation'] = data['nation'].astype('category')
data['approach'] = data['approach'].astype('category')
data['route1'] = data['route1'].astype('category')
data['route2'] = data['route2'].astype('category')
data['route3'] = data['route3'].astype('category')

print(data.info())

data.to_csv('cleaned_expeditions_data.csv', index=False)
