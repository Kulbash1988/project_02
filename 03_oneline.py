# Задача 3: Поиск самых высокооплачиваемых работников 

# нужно найти всех сотрудников зарабатывающих по крайней мере 100 0000 долларов в год

employees = {
    "Alice" : 100000,       
    "Bob" : 99817,
    "Carol" : 122908,
    "Frank" : 88123,
    "Eve" : 93121
    }

# вариант 1 - цикл (развернутый)
# Что можно получить из словаря?
print(employees.keys())
print(employees.values())
print(employees.items())
print(tuple(employees))

top_mgrs = []
for name in employees.keys():
    if employees[name] >= 100000:
        top_mgrs.append(name)

print(top_mgrs)       


# вариант 2 - списковые включения (однострочники)
# 1
top_mgrs = [n for n in employees if employees[n] >= 100000]
print(top_mgrs)

#2
top_mgrs = [n for n, s in employees.items() if s >= 100000]
print(top_mgrs)


# Что это
# Как условный оператор записать в одну строку

x = 4
if x > 0:
    print("Больше 0")
else:
    print("Меньше 0") 
print (
     "Больше 0" if x > 0 else "Меньше 0"
     )                      

# используем for
for i in [1, 2, 3]:
    print(i**2)

print(
    [1**2 for i in [1, 2, 3]] # <generator object <genexpr> at 0x000001D8DA40EF60>
) 
