from tkinter import * # 1 импорт
win = Tk() # 2 создали окно
win.geometry("500x300")
win.title("Заголовок")

lab = Label(win, text="ЧВК")
lab.pack()
lab["font"] = ("Times New Roman", # шрифт
               15, # размер
               "bold", # жирный
               "italic", # курсив
               "underline", # подчеркнутый
               "overstrike" # зачеркнутый
               )

def hello():
    print(ent.get()) # получить из Entry
    lab['text'] = ent.get()

btn = Button(win) # однострочный ввод
btn.pack()
btn['text'] = "РЫган"
btn['bg'] = 'pink' # фон
btn['fg'] = 'green' # текст
btn['command'] = hello
btn['bd'] = 5 # ширина рамки
ent = Entry(win)
ent.pack()

win.mainloop() # 3 отображение