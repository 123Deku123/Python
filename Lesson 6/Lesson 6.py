# Функция
#
# def ee(): # объявление функции
#     print("Ы")
#
# ee() # вызов функции
#
# def ss(num1: int, num2: str) -> int: # объявление функции с аргументами
#     """
#     Я покушал с утра и тебе, уважаемый разработчик желаю того же
#     :param num1: число которое ыыыы
#     :param num2: другое число ааа
#     :return:  сумма двух чисел
#     """
#     return num1 + num2 # возврат
#
# print(ss(5, 1)) # вызов с аргументами
# l = [2, 1]
#
# def is_sorted(l: int):
#     if l == sorted(l):
#         print("True")
#     else:
#         print("False")
#
# is_sorted(l)
#
# l = [1, 5, 2]
# print(sorted(l, reverse=True)) # сортировка + перевернуть

# ЛЯМБДА
#
# def add(x, y):
#     return x + y
# # ==
# lfunc = lambda x, y: x + y
# print(lfunc(5 , 4))

# if-else в одну строчку
# answer = input("Лимонад? ").upper()
variants = ("Д", "ДА", "ДЫА")
result = lambda answer: True if answer in variants else False
print(result(answer=input("Лимонад? ".upper())))