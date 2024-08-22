import pandas as pd

df = pd.read_csv('2014_Sochi Olympics Nations Medals.csv')
print(df.head())
print(df.info())
print(df.describe())


df = pd.read_csv('dz.csv')
group = df.groupby('City')['Salary'].mean()
print(group)
