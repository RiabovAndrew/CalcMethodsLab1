from scipy.integrate import odeint
import matplotlib.pyplot as plt

class drawing:
    def __init__(self):
        self.X = []
        self.Y = []

class method_runge_kutta:

    def __init__(self, x_0, y_0, to):
        self.h = 0.1
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
        else: self.compare = lambda: self.x < self.to

    def info(self):
        print(self.h, self.x, self.y)

    def function(self, x, y):
        return float(1.2*pow(x, 3) + 3.1*x*y - 2.2)
        # return float(0.9*x*y + 3.5*y - 2.1)
        # return float(x*y)

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
        else: return self.to - self.x


mrk = method_runge_kutta(0, 2, 1)
drawing = drawing()

print("f(", mrk.x, ") = \t", mrk.y, ";\t  step =", mrk.h)
while (mrk.delta() >= 0.000001):
    if mrk.h > mrk.delta(): mrk.h = mrk.delta()
    if abs(mrk.epsilon_h2()) > mrk.epsilon:
        mrk.h = mrk.h / 2
        continue
    mrk.y = mrk.y_i(mrk.h)
    mrk.x = mrk.combinate(mrk.x, mrk.h)
    # drawing.Y.append(mrk.y)
    # drawing.X.append(mrk.x)
    print("f(", mrk.x, ") = \t", mrk.y, ";\t  step =", mrk.h)
    if abs(mrk.epsilon_h() <= mrk.epsilon):
        mrk.h = mrk.h * 2    

# while (mrk.delta() >= 0.000001):
#     if mrk.h > mrk.delta(): mrk.h = mrk.delta()
#     mrk.y = mrk.y_i(mrk.h)
#     mrk.x = mrk.combinate(mrk.x, mrk.h)
#     print("f(", mrk.x, ") = \t", mrk.y, ";\t  step =", mrk.h)




plt.plot(drawing.X, drawing.Y, linewidth = 1.0)
plt.ylabel('some numbers')
#plt.show()