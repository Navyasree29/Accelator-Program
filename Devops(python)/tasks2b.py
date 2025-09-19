'''Task 1: Sum of Numbers 
Write a program using a for loop to calculate the sum of numbers from 1 to 50. 
 
Task 2: Multiplication Table 
Take a number from the user and print its multiplication table (1–10) using a loop. 
 
Task 3: Factorial Calculator 
Use a while loop to find the factorial of a number. 
 
Task 4: Print Patterns 
Use nested loops to print: 
* 
* * 
* * * 
* * * * 
 
Task 5: Prime Number Checker 
Ask user for a number and check if it’s prime or not using a loop. 
 '''
total = 0
for i in range(1, 51):
    total += i
print("Sum from 1 to 50 is:", total)


num = int(input("Enter a number for multiplication table: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

n = int(input("Enter a number to find its factorial: "))
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print(f"Factorial of {n} is: {fact}")


for i in range(1, 5):
    for j in range(i):
        print("*", end=" ")
    print()


num = int(input("Enter a number to check if it is prime: "))
if num <= 1:
    print("Not a prime number")
else:
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number")
