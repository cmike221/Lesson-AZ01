import pandas as pd

# data = [1,2,3,4,5]
# series = pd.Series(data)
# print(series)

# data = {
#     'Name' : ['Alice', 'Bob', 'Roma', 'Anna'],
#     'Age'  : [23, 45, 17, 24],
#     'City' : ['New York', 'LA', 'Chicago', 'Moscow']
# }
#
# df = pd.DataFrame(data)
# print(df)

df = pd.read_csv('World-happiness-report-2024.csv')
# print(df.head(6))
# print(df.tail(4))
# print(df.info())
print(df.describe())
# print(df['Country name'])
# print(df[['Country name', 'Regional indicator']])
# print(df.loc[56])
# print(df.loc[56, 'Healthy life expectancy'])
# print(df[df['Healthy life expectancy'] > 0.7])
