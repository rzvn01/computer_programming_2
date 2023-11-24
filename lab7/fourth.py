def read_numbers_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            numbers_str = file.read()
            numbers = [float(num) for num in numbers_str.split(';') if num.strip()]
            return numbers
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []


def compute_arithmetic_average(numbers):
    return sum(numbers) / len(numbers)


def compute_geometric_average(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product ** (1 / len(numbers))


def print_results(count, average, is_arithmetic):
    if is_arithmetic:
        print(f"Arithmetic Average of {count} numbers:", average)
    else:
        print(f"Geometric Average of {count} numbers:", average)


def main():
    # Get input file path
    file_path = input("Enter the path of the file containing positive rational numbers: ")

    # Read numbers from the file
    numbers = read_numbers_from_file(file_path)

    # Calculate count of numbers
    count = len(numbers)

    # Determine whether to compute arithmetic or geometric average
    is_arithmetic = count > 10

    # Compute the appropriate average
    if is_arithmetic:
        average = compute_arithmetic_average(numbers)
    else:
        average = compute_geometric_average(numbers)

    # Print the results
    print_results(count, average, is_arithmetic)


if __name__ == "__main__":
    main()


# Import the NumPy library and alias it as np
import numpy as np

# Set the size of the square matrix
N = 3

# Create a matrix A filled with zeros of size (N, N)
A = np.zeros((N, N))

# Create a vector B filled with zeros of size N
B = np.zeros(N)

# Fill vector B with random integers from 0 to 9 (10 is exclusive)
for m in range(N):
    B[m] = np.random.randint(10)

# Fill matrix A with random integers from -10 to 9
for m in range(N):
    for n in range(N):
        A[m, n] = np.random.randint(-10, 10)

# Print the matrix A and vector B
print("Matrix A:")
print(A)
print("\nVector B:")
print(B)

# Perform matrix-vector multiplication: C = A * B
C = np.zeros(N)

# Iterate through rows of A
for m in range(N):
    # Iterate through columns of A
    for n in range(N):
        # Update the m-th element of vector C by adding the product of A[m, n] and B[n]
        C[m] += A[m, n] * B[n]

# Print the result vector C
print("\nResult Vector C (Matrix-Vector Multiplication A * B):")
print(C)
