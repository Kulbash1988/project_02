# Задача 1: Последовательность Фибоначчи

# Чему равен 100 элемент?
# 1 2 3 4 5 6    100
# 1 1 2 3 5 8

fib1, fib2 = 1, 1

n = input("Номер элемента ряда Фибоначчи: ")

# Вариант 1 - через цикл while
i = int(n) - 2

while n > 0:
 print(fib2)
 fib1, fib2 = fib2, fib1 + fib2
 i -= 1

print("значение этого элемента:", fib2) 



# Вариант 2 - через цикл for

for i in range(2, int(n)):
 fib1, fib2 = fib2, fib1 + fib2 
 print(fib2)

