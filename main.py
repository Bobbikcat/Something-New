# addition
print('| Сложение |')
try:
    num1 = float(input("Введите первое значение: "))
    num2 = float(input("Введите второе значение: "))
    result = num1 + num2
except ValueError:
    print("Ошибка: Введено не число!")
    print()
else:
    print(f"Результат: {result}")
    print()

# subtraction
print('| Вычитание |')
try:
    num1 = float(input("Введите первое значение: "))
    num2 = float(input("Введите второе значение: "))
    result = num1 - num2
except ValueError:
    print("Ошибка: Введено не число!")
    print()
else:
    print(f"Результат: {result}")
    print()

# multiplication
print('| Умножение |')
try:
    num1 = float(input("Введите первое значение: "))
    num2 = float(input("Введите второе значение: "))
    result = num1 * num2
except ValueError:
    print("Ошибка: Введено не число!")
    print()
else:
    print(f"Результат: {result}")
    print()

# division
print('| Деление |')
try:
    num1 = float(input("Введите первое значение: "))
    num2 = float(input("Введите второе значение: "))
    result = num1 / num2
except ValueError:
    print("Ошибка: Введено не число!")
except ZeroDivisionError:
    print("Ошибка: Деление на ноль!")
else:
    print(f"Результат: {result}")
finally:
    print()
    print("Завершение работы..")
