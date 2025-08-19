def add(x,y):
    """Returns the sum of x and y."""
    return x + y
def subtract(x,y): 
    """Returns the difference of x and y."""
    return x - y
def multiply(x,y):
    """Returns the product of x and y."""
    return x * y
def divide(x,y):
    """Returns the quotient of x and y."""
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y
def power(x,y):
    """Returns x raised to the power of y."""
    return x ** y
def percent(x,y):
    """Returns y percent of x."""
    return (x * y) / 100
print("Calculator module loaded. You can now use the functions: \n1.Add(+) \n2.Subtract(-) \n3.Multiply(*) \n4.Divide(/) \n5.Power(^) \n6.Percentage(%)")
operators = input("Enter the operator you want to use: ")
if operators not in ['+', '-', '*', '/', '^', '%']:
    raise ValueError("Invalid operator. Please use one of the following: +, -, *, /, ^, %")
x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))
if operators == '+':
    print(f"The result is: {add(x, y)}")
elif operators == '-':
    print(f"The result is: {subtract(x, y)}")
elif operators == '*':
    print(f"The result is: {multiply(x, y)}")
elif operators == '/':
    try:
        print(f"The result is: {divide(x, y)}")
    except ValueError as e:
        print(e)
elif operators == '^':
    print(f"The result is: {power(x, y)}")
elif operators == '%':
    print(f"{y}% of {x} is: {percent(x, y)}")
print("Thank you for using the Calculator module!")