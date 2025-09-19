# Task 1: Number Check
number = int(input())
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# Task 2: Even or Odd
num = int(input())
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# Task 3: Simple Calculator
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == '+':
    print("Result:", num1 + num2)
elif operator == '-':
    print("Result:", num1 - num2)
elif operator == '*':
    print("Result:", num1 * num2)
elif operator == '/':
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Invalid operator.")

# Task 4: Voting Eligibility
age = int(input("Enter your age: "))
if age >= 18:
    print("Eligible to Vote.")
else:
    print("Not Eligible to Vote.")

# Task 5: Grade Evaluator
marks = float(input("Enter your marks: "))
if marks >= 90:
    print("Grade A")    
elif marks >= 75:
    print("Grade B")
elif marks >=50:
    print("Grade C")
else :
    print("Fail")