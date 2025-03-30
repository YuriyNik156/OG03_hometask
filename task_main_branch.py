# Напишите функцию, которая вычисляет факториал числа с использованием цикла.

def factorial(a):
    if not isinstance(a, int) or a < 0: # Проверяем, является ли число целым и неотрицательным
        raise ValueError ("Введите целое положительное число для нахождения факториала")

    result = 1
    for i in range(1, a + 1):
        result *= i
    return result

try:
    print(factorial(-5.7))

except (ValueError, TypeError) as e:
    print(f"Ошибка: {e}")


