#Calculator that prints results formatted.
"""
1. Save num1, symbol, and num2 from multiple expressions
3. Switch of symbols to perform expression
4. Print answer
"""

print("\nWelcome to my Calculator!\n\n")

num1 = input("Enter your 1st number: ")
symbol = input("Enter the operation (+, -, *, /): ")
num2 = input("Enter your second number: ")


if symbol == '+':
    answer = int(num1)+int(num2)
elif symbol == "-":
    answer = int(num1)-int(num2)
elif symbol == '*':
    answer = int(num1)*int(num2)
elif symbol == '/':
    if num2 == 0:
        print("Error: division by zero")
    answer = float(num1)/float(num2)
else:
    print("Error: Invalid operation")

print(num1, " ", symbol, " ", num2, " = ", answer)

