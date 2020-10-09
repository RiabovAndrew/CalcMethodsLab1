import numpy as np
from prettytable import PrettyTable
import matplotlib.pyplot as plt
from config import x_0
from config import y_0
from config import h
from config import to

class accurate_method:

    def __init__(self, x_0, y_0, to, h):
        self.h = h
        self.to = to
        self.x = float(x_0)
        self.y = float(y_0)
        self.epsilon = 0.0001
        if to <= x_0:
            self.combinate = lambda a, b: a - b
        else:
            self.combinate = lambda a, b: a + b
        if to < x_0:
            self.compare = lambda: self.x > self.to
        else:
            self.compare = lambda: self.x < self.to

    def info(self):
        print(self.h, self.x, self.y)

    def function(self, x, y):
        return float(1.2*pow(x, 3) + 3.1*x*y - 2.2)
        # return float(0.9*x*y + 3.5*y - 2.1)

    def __fi_0(self, h):
        return h*self.function(self.x, self.y)

    def __fi_1(self, h):
        return h*self.function(self.combinate(self.x, h/2), self.combinate(self.y, self.__fi_0(h)/2))

    def __fi_2(self, h):
        return h*self.function(self.combinate(self.x, h/2), self.combinate(self.y, self.__fi_1(h)/2))

    def __fi_3(self, h):
        return h*self.function(self.combinate(self.x, h), self.combinate(self.y, self.__fi_2(h)))

    def y_i(self, h):
        return self.combinate(self.y, (self.__fi_0(h) + 2*self.__fi_1(h) + 2*self.__fi_2(h) + self.__fi_3(h))/6)

    def epsilon_h(self):
        tmp_y = self.y
        tmp_x = self.x
        self.y = self.y_i(self.h/2)
        self.x = self.combinate(self.x, self.h/2)
        y_h2 = self.y_i(self.h/2)
        self.y = tmp_y
        self.x = tmp_x
        y_h = self.y_i(self.h)
        return (y_h2 - y_h)*pow(2, 3)/(pow(2, 3) - 1)

    def epsilon_h2(self):
        tmp_y = self.y
        tmp_x = self.x
        self.y = self.y_i(self.h/2)
        self.x = self.combinate(self.x, self.h/2)
        y_h2 = self.y_i(self.h/2)
        self.y = tmp_y
        self.x = tmp_x
        y_h = self.y_i(self.h)
        return (y_h2 - y_h)/(pow(2, 3) - 1)

    def delta(self):
        if self.to < self.x:
            return self.x - self.to
        else:
            return self.to - self.x

class method_runge_kutta:

    def __init__(self, x_0, y_0, to, h):
        self.h = h
        self.to = to
        self.x = float(x_0)
        self.y = float(y_0)
        self.epsilon = 0.001
        if to <= x_0:
            self.combinate = lambda a, b: a - b
        else:
            self.combinate = lambda a, b: a + b
        if to < x_0:
            self.compare = lambda: self.x > self.to
        else:
            self.compare = lambda: self.x < self.to

    def info(self):
        print(self.h, self.x, self.y)

    def function(self, x, y):
        return float(1.2*pow(x, 3) + 3.1*x*y - 2.2)
        # return float(0.9*x*y + 3.5*y - 2.1)

    def __fi_0(self, h):
        return h*self.function(self.x, self.y)

    def __fi_1(self, h):
        return h*self.function(self.combinate(self.x, h/2), self.combinate(self.y, self.__fi_0(h)/2))

    def __fi_2(self, h):
        return h*self.function(self.combinate(self.x, h), self.combinate(self.y, -self.__fi_0(h) + 2*self.__fi_1(h)))

    def y_i(self, h):
        return self.combinate(self.y, (self.__fi_0(h) + 4*self.__fi_1(h) + self.__fi_2(h))/6)

    def epsilon_h(self):
        tmp_y = self.y
        tmp_x = self.x
        self.y = self.y_i(self.h/2)
        self.x = self.combinate(self.x, self.h/2)
        y_h2 = self.y_i(self.h/2)
        self.y = tmp_y
        self.x = tmp_x
        y_h = self.y_i(self.h)
        return (y_h2 - y_h)*pow(2, 3)/(pow(2, 3) - 1)

    def epsilon_h2(self):
        tmp_y = self.y
        tmp_x = self.x
        self.y = self.y_i(self.h/2)
        self.x = self.combinate(self.x, self.h/2)
        y_h2 = self.y_i(self.h/2)
        self.y = tmp_y
        self.x = tmp_x
        y_h = self.y_i(self.h)
        return (y_h2 - y_h)/(pow(2, 3) - 1)

    def delta(self):
        if self.to < self.x:
            return self.x - self.to
        else:
            return self.to - self.x


class drawing(method_runge_kutta):

    def __init__(self):
        self.X_I = []
        self.Y_I = []
        self.X_A = []
        self.Y_A = []

class table:

    def __init__(self):
        self.X_I = []
        self.Step_I = []
        self.Y_I = []
        self.Error_I = []
        self.X_A = []
        self.Step_A = []
        self.Y_A = []


# Инициализация нужных переменных
mrk = method_runge_kutta(x_0(), y_0(), to(), h())
am = accurate_method(x_0(), y_0(), to(), h())
table = table()
drawing = drawing()
tbl = PrettyTable()

tbl.field_names = ["\033[36mX\033[0m", "\033[36mШаг\033[0m", "\033[36mНеточный Y\033[0m"]
tbl.add_row(["\033[33m" + str(mrk.x) + "\033[0m", "\033[33m" + str(mrk.h) + "\033[0m", "\033[33m" + str(mrk.y) + "\033[0m"])

drawing.Y_I.append(mrk.y)
drawing.X_I.append(mrk.x)
while (mrk.delta() >= 0.000001):
    if mrk.h > mrk.delta():
        mrk.h = mrk.delta()
    if abs(mrk.epsilon_h2()) > mrk.epsilon:
        mrk.h = mrk.h / 2
        continue
    mrk.y = mrk.y_i(mrk.h)
    mrk.x = mrk.combinate(mrk.x, mrk.h)
    drawing.Y_I.append(mrk.y)
    drawing.X_I.append(mrk.x)
    table.X_I.append(mrk.x)
    table.Step_I.append(mrk.h)
    table.Y_I.append(mrk.y)
    if abs(mrk.epsilon_h() <= mrk.epsilon):
        mrk.h = mrk.h * 2

while am.delta() >= 0.000001:
    if am.h > am.delta():
        am.h = am.delta()
    if abs(am.epsilon_h2()) > am.epsilon:
        am.h = am.h / 2
        continue
    am.y = am.y_i(am.h)
    am.x = am.combinate(am.x, am.h)
    table.X_A.append(am.x)
    table.Step_A.append(am.h)
    table.Y_A.append(am.y)
    if abs(am.epsilon_h() <= am.epsilon):
        am.h = am.h * 2



i = 0
for element in table.X_I:
    tbl.add_row(["\033[33m" + str(element) + "\033[0m", "\033[33m" + str(table.Step_I[i]) + "\033[0m", "\033[33m" + str(table.Y_I[i]) + "\033[0m"])
    i += 1
print(tbl)
tbl.clear_rows()



tbl.field_names = ["\033[36mX\033[0m", "\033[36mШаг\033[0m", "\033[36mНеточный Y\033[0m"]
tbl.add_row(["\033[33m1.0\033[0m", "\033[33m0.5\033[0m", "\033[33m0.2\033[0m"])     # Только для моей функции
i = 0
for element in table.X_A:
    tbl.add_row(["\033[33m" + str(element) + "\033[0m", "\033[33m" + str(table.Step_A[i]) + "\033[0m", "\033[33m" + str(table.Y_A[i]) + "\033[0m"])
    i += 1
print(tbl)
tbl = PrettyTable()

am = accurate_method(x_0(), y_0(), to(), h())
while (am.delta() >= 0.000001):
    if am.h > am.delta():
        am.h = am.delta()
    am.y = am.y_i(am.h)
    am.x = round(am.combinate(am.x, am.h), 2)
    table.X_A.append(am.x)
    table.Step_A.append(am.h)
    table.Y_A.append(am.y)

tbl.field_names = ["\033[36mX\033[0m", "\033[36mШаг\033[0m", "\033[36mНеточный Y\033[0m", "\033[36mТочный Y\033[0m", "\033[36mПогрешность\033[0m"]

for element in table.X_I:
    i = table.X_A.index(element)
    i2 = table.X_I.index(element)
    tbl.add_row(["\033[33m" + str(element) + "\033[0m", "\033[33m" + str(table.Step_I[i2]) + "\033[0m", "\033[33m" + str(table.Y_I[i2]) + "\033[0m", "\033[33m" + str(table.Y_A[i]) + "\033[0m", "\033[33m" + str(abs(table.Y_I[i2] - table.Y_A[i])) + "\033[0m"])
print(tbl)

am = accurate_method(x_0(), y_0(), to(), 0.01)
drawing.Y_A.append(am.y)
drawing.X_A.append(am.x)
while (am.delta() >= 0.000001):
    if am.h > am.delta():
        am.h = am.delta()
    am.y = am.y_i(am.h)
    am.x = am.combinate(am.x, am.h)
    drawing.Y_A.append(am.y)
    drawing.X_A.append(am.x)

plt.xlabel("X")
plt.title("Графики приближенного и точного решения")
plt.plot(drawing.X_I, drawing.Y_I, 'r-o', label="Integral", linewidth=1.0)
plt.plot(drawing.X_A, drawing.Y_A, 'b', label="Accurate", linewidth=1.0)
plt.ylabel("F[x, f(x)]")
plt.grid(True)
plt.legend()
plt.show()
