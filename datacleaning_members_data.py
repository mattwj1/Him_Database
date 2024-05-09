import pandas as pd
dtype_spec = {70: 'object'}
members_data = pd.read_csv(
    'members_data.csv',
    dtype=dtype_spec,
    parse_dates=['bcdate'],
    date_parser=lambda x: pd.to_datetime(x, format='%d/%m/%Y', errors='coerce'),
    low_memory=False
)

members_data['expid'] = members_data['expid'].astype('category')
members_data['peakid'] = members_data['peakid'].astype('category')
members_data['membid'] = pd.to_numeric(members_data['membid'], errors='coerce')
members_data['membid'].fillna(method='ffill', inplace=True)
members_data.dropna(subset=['expid', 'peakid', 'bcdate'], inplace=True)


print(members_data.info())
print(members_data.dtypes)
print(members_data.head())

members_data.to_csv('cleaned_members_data.csv', index=False)
