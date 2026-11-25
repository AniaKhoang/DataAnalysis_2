import pandas as pd

print("Задание 4.1")
staff = pd.DataFrame({
    'name':       ['Рома', 'Настя', 'Гриша', 'Света', 'Толя', 'Вика'],
    'dept':       ['IT', 'HR', 'IT', 'IT', 'HR', 'IT'],
    'salary':     [90, 70, 130, 68500, 71500, 95],
    'bonus':      [8.0, 0.0, 12.0, 0.0, 18.0, 0.0],
    'total_comp': [98.0, 70.0, 142.0, 68500.0, 71518.0, 95.0]
})
print(staff, "\n")
print(staff.groupby('dept')['salary'].mean(), "\n")

print("Задание 4.2")
print(staff.groupby('dept').agg({'salary': 'mean', 'bonus': 'max', 'name': 'count'}), "\n")

print("Задание 4.3")
print(pd.pivot_table(staff, values='salary', index='dept', aggfunc='mean'), "\n")

print("Задание 4.4")
t = pd.pivot_table(staff, values='salary', index='dept', aggfunc='mean')
print(t.sort_values('salary', ascending=False), "\n")