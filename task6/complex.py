import math as m


class Complex:

    def __init__(self, real=0, imag=0):
        self.re = real
        self.im = imag

    def conj(self):
        self.im = -self.im

    def abs(self):
        return m.sqrt(self.im * self.im + self.re * self.re)

    def __add__(self, arg):
        c = Complex(self.re + arg.re, self.im + arg.im)
        return c

    def __sub__(self, arg):
        c = Complex(self.re - arg.re, self.im - arg.im)
        return c

    def __mul__(self, arg):
        c = Complex(self.re*arg.re - self.im*arg.im, self.re*arg.im + self.im*arg.re)
        return c

    def __truediv__(self, arg):
        div = self.re * arg.re + arg.im * arg.im
        if div == 0:
            return

        re = self.re * arg.re + self.im * arg.im
        re = re/div

        im = self.im * arg.re - self.re * arg.im
        im = im/div

        c = Complex(re, im)

        return c

    def __eq__(self, arg):
        return self.re == arg.re and self.im == arg.im

    def __ne__(self, arg):
        return self.re != arg.re and self.im != arg.im or self.re != arg.re or self.im != arg.im

    def __lt__(self, arg):
        self_mag = m.sqrt((self.x ** 2) + (self.y ** 2))
        other_mag = m.sqrt((arg.x ** 2) + (arg.y ** 2))
        return self_mag < other_mag

    def __gt__(self, arg):
        self_mag = m.sqrt((self.x ** 2) + (self.y ** 2))
        other_mag = m.sqrt((arg.x ** 2) + (arg.y ** 2))
        return self_mag > other_mag

    def __str__(self):
        return "({:.2f}, j{:.2f})".format(self.re, self.im)
