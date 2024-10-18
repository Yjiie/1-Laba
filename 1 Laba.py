'''
Лабораторная работа №1
Написать программу, которая читая символы из бесконечной последовательности (эмулируется конечным файлом, читающимся поблочно), распознает, преобразует и выводит на экран лексемы по определенному правилу.
Лексемы разделены пробелами. Преобразование делать по возможности через словарь. Для упрощения под выводом числа прописью подразумевается последовательный вывод всех цифр числа.
Регулярные выражения использовать нельзя.
Вариант 14.
Четные двоичные числа, не превышающие 204810, у которых вторая справа цифра равна 0. Выводит на экран цифры числа, исключая нули. Вычисляется среднее число между минимальным и максимальным и выводится прописью.
'''
def digit_to_text(digit):
    words = {
        '0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре',
        '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять'
    }
    return words.get(digit, '')

def binary_to_digits(binary_str):
    return ''.join([digit for digit in binary_str if digit != '0'])

def number_to_words(number):
    return ' '.join([digit_to_text(digit) for digit in str(number)])

def main():
    buffer_size = 1024
    valid_numbers = []

    with open('input.txt', 'r') as file:
        buffer = file.read(buffer_size)
        while buffer:
            tokens = buffer.split()
            for token in tokens:
                if len(token) > 1 and token[-2] == '0' and int(token, 2) % 2 == 0 and int(token, 2) <= 2048:
                    valid_numbers.append(int(token, 2))
                    print(binary_to_digits(token))
            buffer = file.read(buffer_size)

    if len(valid_numbers) > 1:
        min_num = min(valid_numbers)
        max_num = max(valid_numbers)
        avg_num = (min_num + max_num) // 2
        print(f"Среднее число между {min_num} и {max_num} - {avg_num} прописью: {number_to_words(avg_num)}")
    else:
        print("Недостаточно чисел для вычисления среднего.")

main()
