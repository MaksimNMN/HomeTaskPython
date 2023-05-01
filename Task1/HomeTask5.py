# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

# a = int(input("Введите число "))
# b = int(input("Введите степень числа положительное число "))
#
# def numb(a, b):
#     if b == 0:
#         return 1
#
#     return a * numb(a, b - 1)
#
# print(numb(a, b))


# Дана строка(возможно,пустая),состоящая из букв
# A-Z: AAAABBBCCXYZDDDDEEEFFFAAAAAABBBB BBBBBBBBBBBBBBBBBBBBBBBB Нужно написать
# функцию  RLE,  которая  на  выходе  даст строку вида:
# A4B3C2XYZD4E3F3A6B28 И сгенерирует ошибку , если
# на вход пришла невалидная строка


# input_str = input('Enter the string: ')

def convert_string(input_str):

    prev_symbol = None
    len_of_series = 0
    result = ""

    for symb in input_str:
        if prev_symbol and symb != prev_symbol:
            result = result + f"{prev_symbol}{len_of_series}"
            len_of_series = 1
        else:
            len_of_series += 1

        prev_symbol = symb

    return result + f"{prev_symbol}{len_of_series}" if prev_symbol else ""


input_str = ""
print(input_str + " -> " + convert_string(input_str))

input_str = "AAABBBCCCXYZA"
print(input_str + " -> " + convert_string(input_str))

input_str = "AAAAAAAAAA"
print(input_str + " -> " + convert_string(input_str))