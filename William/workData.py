import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

fields = ['Landingstidspunkt', 'Bruttovekt']
df = pd.read_csv('fangstdata_2022.csv', sep=';', error_bad_lines=False, usecols=fields)

print("before", df.head())

df['Bruttovekt'] = df['Bruttovekt'].str.replace(',', '.').astype('float64')


n = len(pd.unique(df['Landingstidspunkt']))

df = df.groupby(['Landingstidspunkt']).sum().reset_index()

df['Landingstidspunkt'] = pd.to_datetime(df['Landingstidspunkt'], dayfirst=True)
df = df.sort_values(by=['Landingstidspunkt'], ascending=True)
df.sort_values(by='Landingstidspunkt',ascending=False)
df.to_csv('output.csv', columns = fields)
df.groupby(['Landingstidspunkt'])
## Need to reset data

#df['Landingstidspunkt'].dt.strftime('%m/%d/%Y')

print("after", df)



#df['Bruttovekt'] = df['Bruttovekt'].astype('float64')

#df.plot( 'Landingstidspunkt' , 'Bruttovekt' )

print(n)

