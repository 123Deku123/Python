# l = [] # список(list) - изменяемый
# t = () # кортеж(tuple) - нельзя менять
#
# СЛОВАРИ
# d = {} # пустой словарь
# d["Ботинок"] = "Тяги бархатные" # добавление записи в словарь
# d["Бошмак"] = "Тяги лютые"
# print(d)
# del d["Ботинок"] # удаление записи из словаря
# print(d)
#
# d1 = {
#     "bashmak": "adidas",
#     "bashmak": "nike", # перезапишет значение
#     5: "пять",
#     "bashmak2": "b",
# }
#
# print(d1["bashmak"])
# for key in d1: # перебор ключей
#     print(key)
#
# for v in d1.values(): # перебор значения
#     print(v)
#
# for s in d1.items(): # (ключ, значение)
#     print(s)
#
# for key, val in d1.items():
#     print("[Ключ]:", key, "[Значение]:", val)
#
# l = [4, 1, 7, 3]
# del l[1] # удаление по индексу
# print(l)
#
# del l # удаление значения
#
# values = list(d1.values())
# print(values)
# keys = list(d1.keys())
# print(keys)

# множество -> set
# s = set() # пустое множество
# s1 = {"A", "B", "C"}
# 1) ПОВТОРЕНИЯ ИСКЛЮЧЕНЫ
# 2) нет порядка
# print(s1)

s1 = ["A", "B", "C", "A", "D"]
s2 = set(s1)

if len(s1) != len(s2):
    print(True)