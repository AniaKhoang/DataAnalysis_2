import pandas as pd

print("Задание 3.1")
staff = pd.DataFrame({
    'name':       ['Рома', 'Настя', 'Гриша', 'Света', 'Толя', 'Вика'],
    'dept':       ['IT', 'HR', 'IT', 'IT', 'HR', 'IT'],
    'salary':     [90, 70, 130, 68500, 71500, 95],
    'bonus':      [8, None, 12, None, 18, None],
    'total_comp': [98.0, 70.0, 142.0, 68500.0, 71518.0, 95.0]
})
print(staff, "\n")
print(staff.isna().sum().sum())

print("Задание 3.2")
staff['salary'] = staff.groupby('dept')['salary'].transform(lambda x: x.fillna(x.mean()))
print(staff, "\n")

print("Задание 3.3")
staff['bonus'] = staff['bonus'].fillna(0)
print(staff, "\n")

print("Задание 3.4")
print("Не остались")