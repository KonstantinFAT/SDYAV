import pandas as pd
# Инициализация переменных
full_depth = 0 # Полная глубина зоны заражения
gP = 0 # Предельная глубина зоны заражения
sV = 0 # Площадь зоны возможного заражения
sF = 0 # Площадь зоны фактического заражения
fi = 0 # Угловые размеры зоны возможного заражения
x = 0 # Расстояние до объекта, км
v_st = 0 # Скорость переноса переднего фронта
sF_map = 0 # Площадь разлива фактическая на карте

print("Данная программа позволяет рассчитать зоны повышенного техногенного риска\nпри разливе токсических веществ")
print("При расчете зон повышенного техногенного риска использовалась\nРД 52.04.253-90 (действует на 28.09.2021)")
print("-------------------------------------------------------------")

# Блок расчета эквивалентного количества вещества в первичном и вторичном облаках
import calculationQ2 as cQ

# Блок расчета глубины заражения при аварии на химически опасном объекте
print("Определяются по справочным данным.")
print("-------------------------------------------------------------")
import depthQ1
print("-------------------------------------------------------------")
full_depth = depthQ1.depth0_1 + 0.5*depthQ1.depth0_2
print("Полная глубина заражения (км):", full_depth)

# Блок расчета площади зоны заражения СДЯВ
print("Определим площадь зоны возможного заражения.")
v_veter = cQ.numU_1
col_fi = [3]
val_fi = pd.read_excel('./coefficients2.xlsx', usecols = col_fi)
val_fi_list = val_fi.values.tolist()
val_fi_list_new = sum(val_fi_list, []) 
fi = val_fi_list_new[v_veter]
sV = 8.72 * 0.001 * full_depth**2 * fi
print("Площадь возможного заражения составляет (кв.км):", sV)
print("-------------------------------------------------------------")
print("Определим зону фактического заражения.")
k5 = cQ.k0_5
t1 = cQ.t0_1
if k5 == 1:
    k8 = 0.081
if k5 == 0.23:
    k8 = 0.133
if k5 == 0.08:
    k8 = 0.235
sF = k8 * (full_depth**2) * (t1**0.2)
print("Площадь фактического заражения составляет (кв.км):", sF)

# Блок расчета времени подхода зараженного воздуха к объекту и продолжительности поражающего действия СДЯВ
print("Определим время подхода облака СДЯВ.")

import folium
latitude1 = float(input("Введите широту места, где произошел разлив: "))
latitude2 = float(input("Введите широту места заданного объекта: "))
longitude1 = float(input("Введите долготу места, где произошел разлив: "))
longitude2 = float(input("Введите долготу места заданного объекта: "))

map = folium.Map(location = [63.5671, 53.6835], zoom_start = 14)
mark1 = folium.Marker(location = [latitude1, longitude1], popup = "Место разлива", tooltip = 'СДЯВ').add_to(map)
sF_map = folium.vector_layers.Circle(location = [latitude1, longitude1], radius = ((sF/3.14)**(1/2)), popup = None, toolip = None).add_to(map)
mark2 = folium.Marker(location = [latitude2, longitude2], popup = "Точка заданного объекта", tooltip = 'Объект').add_to(map)
if (latitude2 > latitude1):
    x = (latitude2 - latitude1)*111.3
if (latitude1 > latitude2):
    x = (latitude1 - latitude2)*111.3
map.save('map1.html')

stability = cQ.stability_1
if stability == "Инверсия":
    col_st = [4]
    val_st = pd.read_excel('./coefficients2.xlsx', usecols = col_st)
    val_st_list = val_st.values.tolist()
    val_st_list_new = sum(val_st_list, []) 
    v_st = val_st_list_new[v_veter]
if stability == "Изотермия":
    col_st = [5]
    val_st = pd.read_excel('./coefficients2.xlsx', usecols = col_st)
    val_st_list = val_st.values.tolist()
    val_st_list_new = sum(val_st_list, []) 
    v_st = val_st_list_new[v_veter]
if stability == "Конвекция":
    col_st = [6]
    val_st = pd.read_excel('./coefficients2.xlsx', usecols = col_st)
    val_st_list = val_st.values.tolist()
    val_st_list_new = sum(val_st_list, []) 
    v_st = val_st_list_new[v_veter]
t3 = x/v_st
print("Время подхода облака СДЯВ составляет (ч):", t3)
