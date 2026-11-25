import pandas as pd

print("Задание 6.1")
staff = pd.DataFrame({
    'name':       ['Рома', 'Настя', 'Гриша', 'Света', 'Толя', 'Вика', 'Лёша'],
    'dept':       ['IT', 'HR', 'IT', 'IT', 'HR', 'IT', 'IT'],
    'salary':     [90, 70, 130, 68500, 71500, 95, 150],
    'bonus':      [8.0, 0.0, 12.0, 0.0, 18.0, 0.0, 14.0],
    'total_comp': [98.0, 70.0, 142.0, 68500.0, 71518.0, 95.0, 164.0]
})

dep = pd.DataFrame({
    'dept':     ['IT', 'HR', 'Sales'],
    'city':     ['Питер', 'Самара', 'Адлер'],
    'head':     ['Смирнов', 'Кузнецов', 'Морозов']
})

print(staff, "\n")
print(dep, "\n")

top = staff.sort_values('total_comp', ascending=False).head(3)
print(top, "\n")

print("Задание 6.2")
print(staff.groupby('dept')[['salary', 'bonus']].mean(), "\n")

print("Задание 6.3")
share = staff.assign(high=staff['salary'] > 75000).groupby('dept')['high'].mean()
print(share, "\n")