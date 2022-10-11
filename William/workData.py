import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

fields = ['Landingstidspunkt', 'Bruttovekt']
df = pd.read_csv('fangstdata_2022.csv', sep=';', error_bad_lines=False, usecols=fields)

print("before", df['Bruttovekt'].size)

df['Bruttovekt'] = df['Bruttovekt'].str.replace(',', '.').astype('float64')
#df['Bruttovekt'] = df['Bruttovekt'].astype('float64')

#df["Bruttovekt"].plot(kind='hist')

#plt.show()

print("after", df['Bruttovekt'].size)
print(df['Bruttovekt'])
print(df)
