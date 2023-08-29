# Оператор цикла for - перебрать элементы в коллекции
# пример break, continue и pass


room_prices = [41, 94, 100, 7, 21, 92, 62, 49, 37, 17, ]

for price in room_prices:
    if price == max(room_prices): 
        continue
    if price == min(room_prices):
        print('Минимальная цена:', price)
        break
    print('Текущая цена:', price)

print('До свидания!')

# использование pass когда не знаем что писать в конструкции
x = 4
if x > 0:
    pass
elif x < 0:
    pass






# Задача 2
# Напишите код, который принимает список из чисел и возвращает сумму только положительных чисел в нем.

# Например:
# [1,-4,7,12] -> 1 + 7 + 12 = 20

# Примечание:
# если положительных чисел в списке нет, то сумма равна 0.

primes = [1,-4,7,12]

#Вариант 1 - с while
i = 0
total = 0
while i < len(primes):
    if primes[i] >= 0:
        total += primes[i]
    i += 1    

print(total)
    
#Вариант 2 - с for
total = 0
for elem in primes:
    if elem >= 0:
        total += elem

print(total)


# Вариант 3 - с индексы for
# генерация последовательности чисел
# print(list(range(1000, 10000)))

total = 0
for ind in range(len(primes)):
    if primes[ind] >= 0:
        total += primes[ind]

print(total)      


# Вариант 4 - функция enumerate()
total = 0
for ind,elem in enumerate(primes):
    print("Позиция элемент:", ind, "Элемент:", elem)
    if elem >= 0:
        total += elem
print(total)

# Вариант 5 - списковое включение
print(sum([x for x in primes if x > 0]))