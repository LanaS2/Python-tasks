number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))


operation = int(input("Choose operation: 1 for '+', 2 for '-', 3 for '*', 4 for '/': "))


if operation == 1:
    result = number1 + number2
    print("Result:", result)
elif operation == 2:
    result = number1 - number2
    print("Result:", result)
elif operation == 3:
    result = number1 * number2
    print("Result:", result)
elif operation == 4:
    if number2 != 0:
        result = number1 / number2
        print("Result:", result)
    else:
        print("Error: Division by zero is not allowed!")
else:
    print("Invalid operation selected!")

