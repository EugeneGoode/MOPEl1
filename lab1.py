import numpy as np
from random import uniform
from prettytable import PrettyTable


table0 = PrettyTable()
table0.field_names = (["Студент", "Группа"])
name = "Гуденко Євгеній"
group = "ІО-92"
table0.add_row([name, group])
print(table0)

a0 = 3
a1 = 2
a2 = 6
a3 = 4
X = np.empty((8, 3), dtype=float)
Y = np.empty(8)
X0 = np.empty(3)
DX = np.empty(3)
XNormalized = np.empty((8, 3), dtype=float)

for i in range(8):
    for j in range(3):
        X[i, j] = uniform(0, 20)
for i in range(8):
    Y[i] = a0 + a1 * X[i, 0] + a2 * X[i, 1] + a3 * X[i, 2]
for i in range(3):
    X0[i] = (X[:, i].max() + X[:, i].min()) / 2
    DX[i] = X[:, i].max() - X0[i]
Y_min = Y.min()
for i in range(8):
    for j in range(3):
        XNormalized[i, j] = (X[i, j] - X0[j]) / DX[j]
number = -1
for i in range(8):
    if Y[i] == Y_min:
        number = i
X_min = [X[number, 0], X[number, 1], X[number, 2]]

print("X:\n", X)
print("Y:\n", Y)
print("X0: \n", X0)
print("number = ", number)
print("Y_min = ", Y_min)
print("X_min = ", X_min)
print("XNormalized: \n", XNormalized.round(4))