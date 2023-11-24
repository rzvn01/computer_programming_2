import math


class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def magnitude(self):
        return math.sqrt(self.real ** 2 + self.imag ** 2)

    def angle(self):
        return math.degrees(math.atan2(self.imag, self.real))

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real_part, imag_part)

    def __truediv__(self, other):
        denom = other.real ** 2 + other.imag ** 2
        real = (self.real * other.real + self.imag * other.imag) / denom
        imag = (self.imag * other.real - self.real * other.imag) / denom
        return ComplexNumber(real, imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"


if __name__ == "__main__":
    c1 = ComplexNumber(10, 2)
    c2 = ComplexNumber(-1, 20)

    print("Magnitude of c1:", c1.magnitude())
    print("Angle of c1:", c1.angle())

    print("Magnitude of c2:", c2.magnitude())
    print("Angle of c2:", c2.angle())

    sum_result = c1 + c2
    print("Sum of c1 and c2:", sum_result)

    mul_result = c1 * c2
    print("Multiplication of c1 and c2:", mul_result)

    div_result = c1 / c2
    print("Multiplication of c1 and c2:", div_result)
