'''code for csv to db'''

import sqlite3
import pandas as pd

"""
Needed columns (added extra columns tweakeing this week with model)

- strain 
- type
- rating
- effects
- flavor
- description
"""

needed_columns = ['Strain', 'Type', 'Rating', 'Effects', 'Flavor', 'Description']

df_pre = pd.read_csv('https://raw.githubusercontent.com/PT-Med-Cabinet-7/Data-Science/master/Data%20Wrangling/raw_csv/cannabis.csv')

df = pd.DataFrame()

for item in needed_columns:
    df[item] = df_pre[item]

conn= sqlite3.connect('med_cabinet.sqlite3')
curs = conn.cursor()

df.to_sql('strain_info', con=conn)

curs.close()
conn.commit()