# Уравнение Михаэлиса–Ментен – наиболее известная модель фермента-
# тивных кинетических реакций:
# v = d[P] / dt = Vmax[S] / (Km + [S]),
# где v – скорость реакции, преобразующей субстрат S в продукт P и катализиру-
# емой ферментом. Vmax – максимальная скорость реакции (когда все ферменты
# связаны с субстратом S), а константа Михаэлиса Km – это концентрация суб-
# страта, при которой скорость реакции составляет половину от ее максималь-
# ного значения.
# Построить график зависимости v от [S] для реакции при Km = 0.04 М и Vmax =
# 0.1 М/с. Если потребуются метки для осей координат, то загляните в следую-
# щий раздел.
import numpy as np
from matplotlib import patches
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
Vmax = 0.1
Km = 0.4
S = np.linspace(0,20,5000)
v = Vmax * S /(Km + S)
plt.plot(S, v, color = 'r', label = 'Speed of reaction')
ax.hlines(Vmax, 0, 20, label= 'Vmax')
plt.xlabel('Substrate')
plt.ylabel('speed of reaction')
plt.legend(loc = 'lower right')
plt.show()