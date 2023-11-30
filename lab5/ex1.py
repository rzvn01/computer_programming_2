def hex_to_int(hex_value):  # function to return decimal int value
    try:
        return int(hex_value, 16)
    except ValueError:
        raise ValueError("Invalid hex number: {}".format(hex_value))


def hex_calculator():
    try:
        first_operand = input("Enter the first operand (two hex digits): ").upper()
        if not all(c in "0123456789ABCDEF" for c in first_operand):  # check if the input is hexa characters
            raise ValueError("Invalid hex number: {}".format(first_operand))

        operation = input("Enter the operation (+, -, *, /): ")
        if operation not in "+-*/":
            raise ValueError("Invalid operation: {}".format(operation))

        second_operand = input("Enter the second operand (two hex digits): ").upper()
        if not all(c in "0123456789ABCDEF" for c in second_operand):
            raise ValueError("Invalid hex number: {}".format(second_operand))

        int_first = hex_to_int(first_operand)
        int_second = hex_to_int(second_operand)

        if operation == '+':
            result = int_first + int_second
        elif operation == '-':
            result = int_first - int_second
        elif operation == '*':
            result = int_first * int_second
        else:
            if int_second == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            result = int_first / int_second
        if isinstance(result, int):
            print("Result (Hex): {}".format(hex(result).upper()))
        else:
            print("Result (Hex): {}".format(result.hex().upper()))

        print("Result (Decimal): {}".format(result))

    except (ValueError, ZeroDivisionError) as e:
        print("Error:", e)
        hex_calculator()


if __name__ == "__main__":  # call the function
    hex_calculator()
