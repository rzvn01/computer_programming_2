import random
import math


def generate_random_numbers(n):
    return [random.randint(-10, 10) for _ in range(n)]


def apply_function(numbers, is_even):
    if is_even:
        return [math.sin(num * math.pi) for num in numbers]
    else:
        return [math.tan(num * math.pi) for num in numbers]


def print_results(numbers, results):
    print("Results:")
    for num, result in zip(numbers, results):
        print(f"{num} * π => {result}")


def main():
    # Get user input for the count of random numbers
    n = int(input("Enter the count of random numbers (N): "))

    # Generate random numbers
    random_numbers = generate_random_numbers(n)

    # Check if N is even or odd
    is_even = n % 2 == 0

    # Apply sine or tangent function based on even or odd
    results = apply_function(random_numbers, is_even)

    # Print the results
    print_results(random_numbers, results)


if __name__ == "__main__":
    main()
