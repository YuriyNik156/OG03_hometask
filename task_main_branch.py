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

# Напишите функцию, которая принимает список чисел и возвращает наибольшее из них.

def find_number(numbers):
    if not numbers: # Проверяем, что список не пустой
        raise ValueError("В списке должны быть числа")

    max_number = numbers[0] # Начинаем с первого элемента в списке
    for i in numbers:
        if i > max_number:
            max_number = i
    return max_number

numbers = [3, 7, 4, 11, 9, 6, 10]
print(find_number(numbers))
