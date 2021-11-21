import pandas as pd
from calculationQ2 import q_1, numU_1, q0_2

q1 = q_1
q2 = q0_2
v_veter = numU_1

def depth_of_infection():
    nameQ = pd.read_excel('./coefficients3.xlsx') # Открываю excel для чтения файла
    nameQ_list = list(nameQ) # Создаю список заголовков

    # Перебираю список заголовков, оставляю заголовки с числами
    new = []
    for i in nameQ_list:
        if i == 'Unnamed: 0':
            continue
        if i == 'Скорость ветра, м/с':
            continue
        new.append(i)
    Q_list = [float(x) for x in new] # Преобразую в списке все str в float

    # Способ выбора необходимо значения, чтобы обратиться к необходимому столбцу
    q_need = []
    for q in Q_list:
        if (q <= q1): q_need.append(q)
    index_q = Q_list.index(q_need[len(q_need)-1])
    col_Q = [index_q + 2]
    need_Q = pd.read_excel('./coefficients3.xlsx', usecols = col_Q)
    nd_Q_list = need_Q.values.tolist()
    need_Q_list = sum(nd_Q_list, [])
    depth1 = need_Q_list[v_veter]
    print("Глубина зоны заражения для первичного облака составляет (км):", depth1)

    q_need2 = []
    for q in Q_list:
        if (q <= q2): q_need2.append(q)
    index_q2 = Q_list.index(q_need2[len(q_need2)-1])
    col_Q2 = [index_q2 + 2]
    need_Q2 = pd.read_excel('./coefficients3.xlsx', usecols = col_Q)
    nd_Q_list2 = need_Q2.values.tolist()
    need_Q_list2 = sum(nd_Q_list2, [])
    depth2 = need_Q_list2[v_veter]
    print("Глубина зоны заражения для вторичного облака составляет (км):", depth2)
    list_depth = [depth1, depth2]
    return list_depth
list_d = depth_of_infection()
depth0_1 = list_d[0]
depth0_2 = list_d[1]
