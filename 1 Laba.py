'''
Лабораторная работа №1
Написать программу, которая читая символы из бесконечной последовательности (эмулируется конечным файлом, читающимся поблочно), распознает, преобразует и выводит на экран лексемы по определенному правилу.
Лексемы разделены пробелами. Преобразование делать по возможности через словарь. Для упрощения под выводом числа прописью подразумевается последовательный вывод всех цифр числа.
Регулярные выражения использовать нельзя
Вариант 14
Четные двоичные числа, не превышающие 204810, у которых вторая справа цифра равна 0. Выводит на экран цифры числа, исключая нули. Вычисляется среднее число между минимальным и максимальным и выводится прописью.
'''
def digit_to_text(digit):
    digit_dict = {
        '0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре',
        '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять'
    }
    return digit_dict.get(digit, '')

buffer_len = 1
work_buffer = ""
valid_numbers = []

with open("laba.txt", "r") as file:
    buffer = file.read(buffer_len)
    while buffer:
        while buffer >= '0' and buffer <= '9':
            work_buffer += buffer
            buffer = file.read(buffer_len)

        if len(work_buffer) > 0:
            if all(c in "01" for c in work_buffer):
                decimal_value = int(work_buffer, 2)
                if (
                    decimal_value <= 2048 and
                    decimal_value % 2 == 0 and
                    len(work_buffer) > 1 and work_buffer[-2] == '0'
                ):
                    if decimal_value not in valid_numbers:
                        valid_numbers.append(decimal_value)
                        print("Цифры числа, исключая нули:", " ".join(c for c in work_buffer if c != '0'))
            work_buffer = ""

        buffer = file.read(buffer_len)

if valid_numbers:
    min_value = min(valid_numbers)
    max_value = max(valid_numbers)
    avg_value = (min_value + max_value) // 2
    print("Среднее число прописью:", " ".join(digit_to_text(d) for d in str(avg_value)))
else:
    print("Не найдено подходящих чисел.")

