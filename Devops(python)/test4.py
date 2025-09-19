'''4.User Login System 
Problem Statement: 
Your team is automating a simple login system where users can attempt to login. 
They are allowed 3 attempts maximum to enter valid credentials. 
Predefined users and passwords are given. 
Write a Python program that: 
 Prompts for username and password. 
 Displays successful login or locks the account after 3 failed attempts. 
"admin": "admin123", 
"devops_user": "devops2023", 
"tester": "testme"

Sample input and output: 
Enter username: admin 
Enter password: admin12 
Invalid credentials. 
Enter username: devops_user 
Enter password: devop 
Invalid credentials. 
Enter username: tester 
Enter password: test 
Invalid credentials. 
Account locked! 
 
Enter username: tester 
Enter password: testme 
Login successful! 
 
 
 

'''
users = { 
"admin": "admin123", 
"devops_user": "devops2023", 
"tester": "testme" 
} 
attempts = 0 
while attempts < 3: 
    username = input("Enter username: ") 
    password = input("Enter password: ") 
    if username in users and users[username] == password: 
        print("Login successful!") 
        break 
    else: 
        print("Invalid credentials.") 
        attempts += 1 
if attempts == 3: 
    print("Account locked!")