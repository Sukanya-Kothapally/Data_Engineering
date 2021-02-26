import pandas as pd

pd.options.display.max_columns = None
pd.options.display.max_rows = None

df1 = pd.read_csv('COVID_county_data.csv.gz')
coviddf=df1.filter(['date','county','state','cases','deaths'],axis=1)

coviddf['date'] = pd.to_datetime(coviddf['date'])

start='2020-12-01'
end='2020-12-31'

mask=(coviddf['date'] >= start) & (coviddf['date'] <= end)
dec_covid_df=coviddf.loc[mask]
#dec_covid_df.head(5)

groubbycounties_dec =dec_covid_df.groupby(['state','county'])
groubbycounties_dec=groubbycounties_dec.agg({
         'cases': 'max',
         'deaths': 'max'
        })
#groubbycounties_dec.head(5)

groubbycounties_covid =coviddf.groupby(['state','county'])
groubbycounties_covid=groubbycounties_covid.agg({
         'cases': 'max',
         'deaths': 'max'
        })
groubbycounties_covid[['cases_dec', 'deaths_dec']] = groubbycounties_dec[['cases', 'deaths']]
# coviddf.head(5)

groubbycounties_covid.loc[[('Virginia','Loudoun'), ('Oregon','Washington'), ('Kentucky','Harlan'), ('Oregon','Malheur')]]