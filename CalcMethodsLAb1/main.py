class method_runge_kutta:

    def __init__(self, x_0, y_0):
        self.h = 0.1
        self.a = 0
        self.b = 1
        self.x = float(x_0)
        self.y = float(y_0)
        self.epsilon = 0.001

    def info(self):
        print(self.h, self.x, self.y)

    def function(self, x, y):
        # return float(1.2*pow(x, 3) + 3.1*x*y - 2.2)
        return float(x + y)

    def fi_0(self, h):
        return h*self.function(self.x, self.y)

    def fi_1(self, h):
        return h*self.function(self.x + h/2, self.y + self.fi_0(h)/2)

    def fi_2(self, h):
        return h*self.function(self.x + h, self.y - self.fi_0(h) + 2*self.fi_1(h))

    def y_i(self, h):
        return self.y + (self.fi_0(h) + 4*self.fi_1(h) + self.fi_2(h))/6

    def epsilon_h(self):
        tmp_y = self.y
        tmp_x = self.x
        self.y = self.y_i(self.h/2)
        self.x += self.h/2
        y_h2 = self.y_i(self.h/2)
        self.y = tmp_y
        self.x = tmp_x
        y_h = self.y_i(self.h)
        return (y_h2 - y_h)*pow(2, 3)/(pow(2, 3) - 1)
    
    def epsilon_h2(self):
        # self.epsilon_h()/pow(2, 3)        // вариант намного лучше, но мождет возникнуь ошибка из-за маленького числа
        tmp_y = self.y
        tmp_x = self.x
        self.y = self.y_i(self.h/2)
        self.x += self.h/2
        y_h2 = self.y_i(self.h/2)
        self.y = tmp_y
        self.x = tmp_x
        y_h = self.y_i(self.h)
        return (y_h2 - y_h)/(pow(2, 3) - 1)

    def delta(self):
        return self.b - self.x

mrk = method_runge_kutta(0, 2)




while(mrk.x < mrk.b):
    if abs(mrk.epsilon_h2()) > mrk.epsilon:
        mrk.h = mrk.h / 2
        continue
    mrk.y = mrk.y_i(mrk.h)
    mrk.x += mrk.h
    print("f(", mrk.x, ") = ", mrk.y)
    if abs(mrk.epsilon_h() <= mrk.epsilon):
        mrk.h = mrk.h * 2
        #print("step =", mrk.h)

    if abs(mrk.delta()) < 0.000001:
        break
    if mrk.h > mrk.delta(): mrk.h = mrk.delta()

# while(mrk.x <= mrk.b):
#     mrk.y = mrk.y_i(mrk.h)
#     print(mrk.y)
#     mrk.x += mrk.h










