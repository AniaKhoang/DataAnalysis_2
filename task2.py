import pandas as pd

print("Задание 2.1")

staff = pd.DataFrame({
    'name':   ['Рома', 'Настя', 'Гриша', 'Света', 'Толя', 'Вика'],
    'dept':   ['IT', 'HR', 'IT', 'IT', 'HR', 'IT'],
    'salary': [90, 70, 130, 68500, 71500, 95]
})
print(staff, "\n")

it = staff[staff['dept'] == 'IT']
print(it[['name', 'salary']])

print("Задание 2.2")
print(staff.iloc[:3, :2])

print("Задание 2.3")
print(staff[staff['salary'] > 70000])

print("Задание 2.4")
staff['bonus'] = [8, None, 12, None, 18, None]
staff['total_comp'] = staff['salary'] + staff['bonus'].fillna(0)

print(staff, "\n")

print("Задание 2.5")
staff['hire_date'] = ['6', '7', '8', '9', '10', '11']
print(staff, "\n")

staff = staff.drop(columns=['hire_date'])
print(staff, "\n")