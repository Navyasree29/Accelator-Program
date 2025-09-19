'''�
� Task 1: Single Assignment 
 Create a variable called tool_name and assign it the value "Docker". 
 Print: Tool in use: Docker. 
�
� Task 2: Multiple Assignment 
 Assign "Dev", "Test", "Prod" to three variables: env1, env2, env3. 
 Print them in one line: 
 Environments available: Dev, Test, Prod 
�
� Task 3: Same Value Assignment 
 Assign "active" to three variables status1, status2, status3. 
 Print them one by one. 
�
� Task 4: DevOps Mini Scenario 
 Assign: 
o provider = "AWS" 
o region = "ap-south-1" 
o service = "EC2" 
 Print: 
Launching EC2 service in ap-south-1 region on AWS'''

tool_name="Docker"
print("Tool in use : ",tool_name)
env1,env2,env3="Dev","Test","Prod"
print("Environments available: ",env1,env2,env3)
status1,status2,status3="active"
print(status1)
print(status2)
print(status3)
provider = "AWS"
region = "ap-south-1"
service = "EC2"
print("Launching", service, "service in", region, "region on", provider)



''' Variables & Assignments 
1. Assign "Python" to a variable called language and print it. 
2. Assign values 100, 200, 300 to three variables x, y, z in one line. Print them. 
3. Assign the same value 0 to three variables a, b, c. Print their sum. 
�
� Numbers 
1. Write a program that takes two numbers and prints their sum, difference, product, 
and quotient. 
2. Calculate the square and cube of a given number. 
3. Convert temperature from Celsius to Fahrenheit using: 
4. F = (C * 9/5) + 32 
�
� Strings 
1. Take a string input and print it in reverse order. 
2. Count how many vowels are in a given string. 
3. Check if a string is a palindrome (same forwards and backwards). 
�
� Lists 
1. Create a list of 10 numbers and print only the even numbers. 
2. Find the largest and smallest number in a list without using max() or min(). 
3. Merge two lists into one and print the result. 
�
� Tuples 
1. Create a tuple of 5 numbers and calculate their sum. 
2. Check if a given element exists in a tuple. 
3. Convert a tuple into a list, add one element, then convert back to a tuple. 
�
� Dictionaries 
1. Create a dictionary of 3 students with their marks. Print the average marks. 
2. Write a program to count how many times each character appears in a string 
(frequency dictionary). 
Example: "hello" → {'h':1, 'e':1, 'l':2, 'o':1} 
3. Merge two dictionaries into one.
'''
language="Python"
print(language)
x,y,z=100,200,300
print(x,y,z)
a=b=c=0
print(a+b+c)

n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
print("Sum:",n1+n2)
print("Difference:",n1-n2)
print("Product:",n1*n2)
print("Quotient:",n1/n2)

n=int(input("Enter a number: "))
print("Square:",n**2)
print("Cube:",n**3)

c=float(input("Enter temperature in Celsius: "))
f=(c*9/5)+32
print("Fahrenheit:",f)

s=input("Enter a string: ")
print("Reversed:",s[::-1])

vowels="aeiouAEIOU"
count=0
for ch in s:
    if ch in vowels:
        count+=1
print("Vowels:",count)

if s==s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

nums=[1,2,3,4,5,6,7,8,9,10]
for n in nums:
    if n%2==0:
        print(n,end=" ")
print()

lst=[12,5,7,3,25,19]
largest=lst[0]
smallest=lst[0]
for i in lst:
    if i>largest:
        largest=i
    if i<smallest:
        smallest=i
print("Largest:",largest,"Smallest:",smallest)

list1=[1,2,3]
list2=[4,5,6]
merged=list1+list2
print(merged)

t=(10,20,30,40,50)
print("Sum:",sum(t))

elem=int(input("Enter element to search: "))
if elem in t:
    print("Exists")
else:
    print("Not Exists")

t2=(1,2,3)
l=list(t2)
l.append(4)
t2=tuple(l)
print(t2)

students={"A":85,"B":90,"C":80}
avg=sum(students.values())/len(students)
print("Average:",avg)

text=input("Enter a string: ")
freq={}
for ch in text:
    freq[ch]=freq.get(ch,0)+1
print(freq)

d1={"x":1,"y":2}
d2={"z":3,"w":4}
d3={**d1,**d2}
print(d3)
