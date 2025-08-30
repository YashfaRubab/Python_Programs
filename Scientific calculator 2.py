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
    else:
        return x / y
def remainder(x,y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x % y  
def power(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Error! Cannot compute square root of a negative number."
    else:
        return math.sqrt(x)
def cubic_root(x):
    if x < 0:
        return "Error! Cannot compute square root of a negative number."
    else:
        return math.cbrt(x)
def sin(x):
    x=math.radians(x)
    return math.sin(x)

def cos(x):
    x=math.radians(x)
    return round(math.cos(x))

def tan(x):
    if x==90:
        print("infinte number")
    else:
     x=math.radians(x)
     return round(math.tan(x))

print("Select operation:")
print("press '+' for Addition")
print("press '-' for Subtraction")
print("press '*' for Multiplication")
print("press '/' for Division")
print("press '%' for Remainder")
print("press '^' for power")
print("press '^^' for square root")
print("press '^^^' for Cubic root")
print("press '<' for Sine function")
print("press '>' for Cosine function")
print("press '</>' for Tan function")
choice = input("Enter choice from:\n '+' \n '-'\n '*'\n '/'\n '%'\n '^'\n '^^'\n '^^^'\n '<'\n '>'\n '</>'\n\r")
if choice == '+' or choice == '-' or choice == '*' or choice == '/' or choice == '%' or choice == '^':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '+':
            print(add(num1, num2))
        elif choice == '-':
            print(subtract(num1, num2))
        elif choice == '*':
            print(multiply(num1, num2))
        elif choice == '/':
            print(divide(num1, num2))
        elif choice == '^':
            print(power(num1, num2))
        elif choice == '%':
            print(remainder(num1,num2))
elif choice == '^^' or choice == '^^^' or choice == '<' or choice == '>' or choice == '</>':
        num = float(input("Enter the number: "))
        if choice == '^^':
            print(square_root(num))
        elif choice == '^^^':
            print(cubic_root(num))
        elif choice == '<':
            print(sin(num))
        elif choice == '>':
            print(cos(num))
        elif choice == '</>':
            print(tan(num))
else:
    print("Invalid Input")