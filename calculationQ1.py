# Блок расчета эквивалентного количества вещества в первичном облаке
# Инициализация переменных
q_1 = 0 # Эквивалентное количество вещества в СДЯВ.
k1 = 0 # Коэффициент, зависящий от условий хранения СДЯВ.
k3 = 0 # Коэффициент, равный отношению пороговой токсодозы хлора к пороговой токсодозе другого СДЯВ
k5 = 0 # Коэффициент, учитывающий степень вертикальной устойчивости атмосферы.
k7 = 0 # Коэффициент, учитывающий влияние температуры воздуха.
q0 = 0 # Количество выброшенного при аварии вещества, т.
spot = 0 # Место, где произошел разлив.
d = 0 # Плотность СДЯВ, т/куб.м
vx = 0 # Объем хранилища, куб.м
n = 0 # Содержание СДЯВ в природном газе, %
vg = 0 # Объем секции газопровода между автоматическими отсекателями, куб.м
temp = 0 # Температура воздуха, гр.Цельсия

import pandas as pd

def q1():
    print("Для начала необходимо рассчитать зоны заражения СДЯВ.")
    spot = input("Где произошел выброс СДЯВ? Напишите Хранилище или Газопровод: ")
    print("------------------------------------------------------")
    print("Степень вертикальной устойчивости атмосферы. Написать ниже Инверсия, Изотермия, Конвекция (один из вариантов).")
    print("------------------------------------------------------")
    stability = input()
    if(stability == "Инверсия"):
        k5 = 1
    elif(stability == "Изотермия"):
        k5 = 0.23
    else:
        k5 = 0.08
    print("Какая температура воздуха? Напишите ниже (в градусах Цельсия)")
    print("------------------------------------------------------")
    temp = float(input())
    print("Какой СДЯВ разлился в результате аварии?")
    print("------------------------------------------------------")
    col_nameCDYAV = [1]
    nameCDYAV = pd.read_excel('./coefficients.xlsx', usecols = col_nameCDYAV)
    print(nameCDYAV.head(35))
    print("Выбирите необходимый СДЯВ и напишите его номер ниже.")
    numCDYAV = int(input())
    col_d = [3]
    val_d = pd.read_excel('./coefficients.xlsx', usecols = col_d)
    val_d_list = val_d.values.tolist() # Преобразование столбца в список списков
    val_d_list_new = sum(val_d_list, []) # Преобразование списка списков в список поплавков
    d = val_d_list_new[numCDYAV]
    col_k1 = [6]
    val_k1 = pd.read_excel('./coefficients.xlsx', usecols = col_k1)
    val_k1_list = val_k1.values.tolist()
    val_k1_list_new = sum(val_k1_list, [])
    k1 = val_k1_list_new[numCDYAV]
    col_k3 = [8]
    val_k3 = pd.read_excel('./coefficients.xlsx', usecols = col_k3)
    val_k3_list = val_k3.values.tolist()
    val_k3_list_new = sum(val_k3_list, [])
    k3 = val_k3_list_new[numCDYAV]
    if (temp <= (-40)):
        col_k7 = [9]
        val_k7 = pd.read_excel('./coefficients.xlsx', usecols = col_k7)
        val_k7_list = val_k7.values.tolist()
        val_k7_list_new = sum(val_k7_list, [])
        k7 = val_k7_list_new[numCDYAV]
    elif (temp > (-40) and temp < (-20)):
        col_k7 = [10]
        val_k7 = pd.read_excel('./coefficients.xlsx', usecols = col_k7)
        val_k7_list = val_k7.values.tolist()
        val_k7_list_new = sum(val_k7_list, [])
        k7 = val_k7_list_new[numCDYAV]
    elif (temp > (-20) and temp < 0):
        col_k7 = [11]
        val_k7 = pd.read_excel('./coefficients.xlsx', usecols = col_k7)
        val_k7_list = val_k7.values.tolist()
        val_k7_list_new = sum(val_k7_list, [])
        k7 = val_k7_list_new[numCDYAV]
    elif (temp > 0 and temp < 20):
        col_k7 = [12]
        val_k7 = pd.read_excel('./coefficients.xlsx', usecols = col_k7)
        val_k7_list = val_k7.values.tolist()
        val_k7_list_new = sum(val_k7_list, [])
        k7 = val_k7_list_new[numCDYAV]
    else:
        col_k7 = [13]
        val_k7 = pd.read_excel('./coefficients.xlsx', usecols = col_k7)
        val_k7_list = val_k7.values.tolist()
        val_k7_list_new = sum(val_k7_list, [])
        k7 = val_k7_list_new[numCDYAV]
       
    if (spot == "Хранилище"):
        vx = float(input("Укажите объем хранилища, куб.м: "))
        q0 = d * vx
    else:
        n = float(input("Укажите концентрацию СДЯВ в природном газе, %: "))
        vg = float(input("Укажите объем секции газопровода м/у авоматическими отсекателями, куб.м: "))
        q0 = (n * d * vg) / 100    
    print("------------------------------------------------------")
    q_1 = k1*k3*k5*k7*q0
    print("Эквивалентное количество вещества в первичном облаке составляет -", q_1)
    list_q1 = [k1, k3, k5, k7, q0, q_1, d, numCDYAV, temp, stability]
    return list_q1
_list = q1()
k1_1 = _list[0]
k3_1 = _list[1]
k5_1 = _list[2]
k7_1 = _list[3]
q0_1 = _list[4]
q00_1 = _list[5]
d_1 = _list[6]
numCDYAV_1 = _list[7]
temp_1 = _list[8]
stability0_1 = _list[9]
