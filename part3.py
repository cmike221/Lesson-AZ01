import pandas as pd

df = pd.read_csv('animal.csv')
print(df)
# inplace=True применяет изменения к исходному файлу
# df.dropna(inplace=True)             # удаляет строки без данных

# df.fillna(0, inplace=True)    # заполняет пустые поля данными
# print(df)

group = df.groupby('Пища')['Средняя продолжительность жизни'].mean()
print(group)

df.to_csv('output.csv', index=False)
