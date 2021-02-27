import pandas as pd

pd.options.display.max_columns = None
pd.options.display.max_rows = None

df = pd.read_csv('acs2017_census_tract_data.csv.gz')
censusdf=df.filter(['County','State','TotalPop','IncomePerCap','Poverty'],axis=1)
censusdf['County'] = censusdf['County'].map(lambda k:k.strip('County').strip())
#censusdf.head(5)

censusdf.rename(columns={'State':'state','County':'county'},inplace=True)# Did for integration purpose

groubbycounties_census =censusdf.groupby(['state','county'])
groubbycounties_census=groubbycounties_census.agg({
         'TotalPop': 'sum',
         'IncomePerCap': 'mean',
         'Poverty': 'mean' })

groubbycounties_census.loc[[('Virginia','Loudoun'), ('Oregon','Washington'), ('Kentucky','Harlan'), ('Oregon','Malheur')]]
