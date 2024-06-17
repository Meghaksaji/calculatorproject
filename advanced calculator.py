import math


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y


def exponentiate(x, y):
    return x ** y


def square_root(x):
    if x < 0:
        return "Error! Square root of a negative number."
    return math.sqrt(x)


def sine(x):
    return math.sin(math.radians(x))


def cosine(x):
    return math.cos(math.radians(x))


def tangent(x):
    return math.tan(math.radians(x))


print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exponentiate")
print("6. Square Root")
print("7. Sine")
print("8. Cosine")
print("9. Tangent")

while True:
    choice = input("Enter choice (1/2/3/4/5/6/7/8/9): ")

    if choice in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
        if choice in ('1', '2', '3', '4', '5'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(num1, "+", num2, "=", add(num1, num2))

            elif choice == '2':
                print(num1, "-", num2, "=", subtract(num1, num2))

            elif choice == '3':
                print(num1, "*", num2, "=", multiply(num1, num2))

            elif choice == '4':
                print(num1, "/", num2, "=", divide(num1, num2))

            elif choice == '5':
                print(num1, "^", num2, "=", exponentiate(num1, num2))

        elif choice == '6':
            num = float(input("Enter number: "))
            print("Square root of", num, "=", square_root(num))

        elif choice in ('7', '8', '9'):
            angle = float(input("Enter angle in degrees: "))

            if choice == '7':
                print("Sine of", angle, "degrees =", sine(angle))

            elif choice == '8':
                print("Cosine of", angle, "degrees =", cosine(angle))

            elif choice == '9':
                print("Tangent of", angle, "degrees =", tangent(angle))

        break
    else:
        print("Invalid input")
