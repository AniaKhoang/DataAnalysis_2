import pandas as pd

print("Задание 1.1")
ser = pd.Series([12, 24, 36, 48, 60], index=[1, 3, 0, 4, 2])
print(ser)

print("\nЗадание 1.2")
df = pd.DataFrame({
    'name': ['Дима', 'Оля', 'Костя', 'Юля'],
    'age': [19, 20, 21, 22],
})
print(df)

print("\nЗадание 1.3")
print(df.head(1), "\n")
print(df.tail(1), "\n")
print(df.dtypes, "\n")
print(df.describe(), "\n")