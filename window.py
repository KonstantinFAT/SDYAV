from tkinter import *
from tkinter.ttk import Combobox, Checkbutton

def clicked():
    res = 'Привет, {}'.format(txt.get())
    lbl.configure(text = res)

window = Tk() # Создание окна
window.geometry('600x300') # Размеры окна
window.title("Добро пожаловать в приложение PythonRu")

chk_state = BooleanVar()
chk_state.set(True)
chk = Checkbutton(window, text = "Выбрать", var = chk_state) # Создание чекбокса
chk.grid(column = 2, row = 0)

combo = Combobox(window) # Виджет поля с выпадающим окном
combo['values'] = (1, 2, 3, 4, 5, 'текст')
combo.current(1)
combo.grid(column = 0, row = 2)

lbl = Label(window, text = "Привет!", font = ('Times New Roman', 25)) # Создание текста
lbl.grid(column = 0, row = 0)

btn = Button(window, text = "Клик!", fg = 'green', bg = 'yellow', command = clicked) # Создание кнопки
btn.grid(column = 1, row = 0)

txt = Entry(window, width = 10) # Поле ввода
txt.focus() # Поле фокуса
txt.grid(column = 0, row = 1)
window.mainloop()
