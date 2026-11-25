import pandas as pd

print("Задание 5.1")
staff = pd.DataFrame({
    'name':       ['Рома', 'Настя', 'Гриша', 'Света', 'Толя', 'Вика'],
    'dept':       ['IT', 'HR', 'IT', 'IT', 'HR', 'IT'],
    'salary':     [90, 70, 130, 68500, 71500, 95],
    'bonus':      [8.0, 0.0, 12.0, 0.0, 18.0, 0.0],
    'total_comp': [98.0, 70.0, 142.0, 68500.0, 71518.0, 95.0]
})

dep = pd.DataFrame({
    'dept':     ['IT', 'HR', 'Sales'],
    'city':     ['Питер', 'Самара', 'Адлер'],
    'head':     ['Смирнов', 'Кузнецов', 'Морозов']
})

print(staff, "\n")
print(dep, "\n")

print("Задание 5.2")
df = staff.rename(columns={'dept': 'department'})
managers = dep.rename(columns={'dept': 'department'})

m = df.merge(managers, on='department', how='left')
print(m, "\n")

print("Задание 5.3")
new = pd.DataFrame({
    'name':       ['Рома'],
    'dept':       ['IT'],
    'salary':     [150],
    'bonus':      [14.0],
    'total_comp': [164.0]
})

staff = pd.concat([staff, new], ignore_index=True)
print(staff, "\n")

print("Задание 5.4")
staff = staff.reset_index(drop=True)
print(staff, "\n")