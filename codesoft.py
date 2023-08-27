#addition
def add(x, y):
    return x + y
#substraction
def subtract(x, y):
    return x - y
#multiplication
def multiply(x, y):
    return x * y
#division
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Cannot divide by zero."
#calculator_opration
def calculator():
    print("Simple Calculator")
    print("Operations:")
    print("1. Add")
    print("2. Sub")
    print("3. Multiplication")
    print("4. Division")
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = int(input("Enter the operation choice (1/2/3/4): "))
        if operation == 1:
            result = add(num1, num2)
        elif operation == 2:
            result = subtract(num1, num2)
        elif operation == 3:
            result = multiply(num1, num2)
        elif operation == 4:
            result = divide(num1, num2)
        else:
            print("Invalid operation choice.")
            return
        print("Result: ", result)
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
if __name__ == "__main__":
    calculator()
