import pandas as pd

integrated_df= groubbycounties_census.join(groubbycounties_covid)

integrated_df['Totalcases'] = integrated_df.apply(lambda index: (index['cases'] * 100000) / index['TotalPop'], axis=1)
integrated_df['Totaldeaths'] = integrated_df.apply(lambda index: (index['deaths'] * 100000) / index['TotalPop'], axis=1)
#integrated_df.head(5)
