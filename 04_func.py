# Функция - это блок кода, который можно вызывать с разными параметрами

employees_1 = {
    "Alice" : 100000,       
    "Bob" : 99817,
    "Carol" : 122908,
    "Frank" : 88123,
    "Eve" : 93121
    }
employees_2 = {
    "Nikita" : 1,       
    "Masha" : 110000,
    "Matvey" : 90000,
    "Sasha" : 88123,
    "Tanya" : 193121
    }



# Этап создания функций 
# Вариант c print
def get_topmgrs(empl):
    top_mgrs = [n for n, s in empl.items() if s >= 100000]
    print(top_mgrs)

# Этап вызова функции
get_topmgrs(employees_1)
get_topmgrs(employees_2)


# для того что бы воспользоваться результатом функции воспользуемся return

def get_topmgrs(empl):
    return [n for n, s in empl.items() if s >= 100000]

print([employees_1[i]*1.5 for i in get_topmgrs(employees_1)])