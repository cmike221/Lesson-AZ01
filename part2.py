import pandas as pd

df = pd.read_csv('hh.csv')

df['Test'] = [new for new in range(1072)]  # Добавили колонку Test
print(df)
df.drop('Test', axis=1, inplace=True)  # Удалили колонку Test
print(df)

df.drop(1070, axis=0, inplace=True)  # Удалили строку Rust Developer
print(df)
