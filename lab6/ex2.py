import random

from lab6.ex1 import ComplexNumber  # import the class to  not duplicate the code


class ComplexVector:
    def __init__(self, dimension, elements=None):
        self.dimension = dimension
        if elements is None:
            self.elements = [self._generate_random_complex() for _ in range(dimension)]
        else:
            if len(elements) != dimension:
                raise ValueError("Number of elements must match the dimension.")
            self.elements = elements

    def _generate_random_complex(self):
        real_part = random.randint(-10, 10)
        imag_part = random.randint(-10, 10)
        return ComplexNumber(real_part, imag_part)

    def magnitude(self):
        return sum(element.magnitude() ** 2 for element in self.elements) ** 0.5

    def add(self, other_vector):
        if self.dimension != other_vector.dimension:
            raise ValueError("Vectors must have the same dimension for addition.")
        new_elements = [self.elements[i] + other_vector.elements[i] for i in range(self.dimension)]
        return ComplexVector(self.dimension, new_elements)

    def multiply(self, other_vector):
        if self.dimension != other_vector.dimension:
            raise ValueError("Vectors must have the same dimension for multiplication.")
        new_elements = [self.elements[i] * other_vector.elements[i] for i in range(self.dimension)]
        return ComplexVector(self.dimension, new_elements)

    def highest_magnitude_element(self):
        max_magnitude = -1
        max_index = -1
        for i, element in enumerate(self.elements):
            mag = element.magnitude()
            if mag > max_magnitude:
                max_magnitude = mag
                max_index = i
        return max_index

    def __str__(self):
        elements_str = ", ".join(str(element) for element in self.elements)
        return f"Dimension: {self.dimension}, Elements: [{elements_str}]"


if __name__ == "__main__":
    vector1 = ComplexVector(5)
    vector2 = ComplexVector(5)
    print("Vector 1:", vector1)
    print("Vector 2:", vector2)

    print("Magnitude of Vector 1:", vector1.magnitude())

    sum_vector = vector1.add(vector2)
    print("Sum of Vector 1 and Vector 2:", sum_vector)

    product_vector = vector1.multiply(vector2)
    print("Product of Vector 1 and Vector 2:", product_vector)

    max_magnitude_position = vector1.highest_magnitude_element()
    print("Position of element with highest magnitude in Vector 1:", max_magnitude_position)
