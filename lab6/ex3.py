import random

from lab6.ex2 import ComplexVector, ComplexNumber


class ComplexMatrix(ComplexVector):
    def __init__(self, rows, cols, elements=None):
        self.rows = rows
        self.cols = cols
        if elements is None:
            super().__init__(rows * cols)
        else:
            if len(elements) != rows * cols:
                raise ValueError("Number of elements must match the matrix dimensions.")
            super().__init__(rows * cols, elements)

    def transpose(self):
        transposed_elements = [self.elements[j * self.cols + i] for i in range(self.cols) for j in range(self.rows)]
        return ComplexMatrix(self.cols, self.rows, transposed_elements)

    def matrix_multiply(self, other_matrix):
        if self.cols != other_matrix.rows:
            raise ValueError("Matrix dimensions are not suitable for multiplication.")
        result = ComplexMatrix(self.rows, other_matrix.cols)
        for i in range(self.rows):
            for j in range(other_matrix.cols):
                dot_product = ComplexNumber(0, 0)
                for k in range(self.cols):
                    dot_product += self.get_element(i, k) * other_matrix.get_element(k, j)
                result.set_element(i, j, dot_product)
        return result

    def get_element(self, row, col):
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            raise ValueError("Row or column index out of bounds.")
        return self.elements[row * self.cols + col]

    def set_element(self, row, col, value):
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            raise ValueError("Row or column index out of bounds.")
        self.elements[row * self.cols + col] = value

    def __str__(self):
        matrix_str = "\n".join(
            "[" + " ".join(str(self.get_element(i, j)) for j in range(self.cols)) + "]" for i in range(self.rows))
        return matrix_str


if __name__ == "__main__":
    matrix1 = ComplexMatrix(2, 2)
    matrix2 = ComplexMatrix(2, 2)

    print("Matrix 1:")
    print(matrix1)
    print("Matrix 2:")
    print(matrix2)

    transpose_matrix = matrix1.transpose()
    print("Transposed Matrix 1:")
    print(transpose_matrix)

    product_matrix = matrix1.matrix_multiply(matrix2)
    print("Product of Matrix 1 and Matrix 2:")
    print(product_matrix)
