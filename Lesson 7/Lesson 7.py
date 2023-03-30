# ==== ЗАПИСЬ В TXT ====
from typing import TextIO

# f = open("file.txt", "w", encoding="utf-8") # на запись
# f.write("Я ломал лицо\nЯ ломал лицо")
# f.close()

# ==== ЧТЕНИЕ TXT ====
# f = open("file.txt", "r", encoding="utf-8") # на чтение
# content = f.read() # чтение из файла
# print(content)
# f.close()

# ==== ЧТЕНИЕ(построное) TXT ====
# try:
#     f = open("file.txt", "r", encoding="utf-8") # на чтение
# except FileExistsError:
#     print("Не фортанууууло")
# else:
#     content = f.readline() # чтение из файла
#     f.close()
#     print(content)
#     summa = 0
#     for number in content:
#         summa = summa + int(number()
#     print(summa)

# f = open("file.txt", "r", encoding="utf-8")
# content = f.read()
# f.close()
# print(content)
# chisla = content.split() # раскадываем по пробелу
# print(chisla)

# JSON
import json
data = [True, None, (1, 5), {1 : "Значение"}, "ENG"]
f = open("file.json", "w", encoding="utf-8")
print(json.dumps(data, ensure_ascii=False)) # ПЕРЕВОДИТ В JS
json.dump(data, f, ensure_ascii=False) # выгрузка в json
f.close()