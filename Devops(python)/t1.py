"""Task 1: Student Grade Management System 
Problem: 
 Ask the user to enter 5 student names and their marks (out of 100). 
 Store them in a dictionary where key = student name and value = marks. 
 Perform the following: 
1. Print the average marks of the class. 
2. Find the highest and lowest scorer. 
3. Display all student names with marks greater than 50. 
Concepts Used: 
 Variables & Multiple Assignments 
 Numbers (marks calculation) 
 Dictionary (key-value storage) 
 Lists (to extract values for average)
"""
students = {}
for i in range(5):
    name = input("student name: ")
    marks = int(input("marks: "))
    students[name] = marks

total = 0
for m in students.values():
    total += m
average = total / 5
print("\nAverage Marks:", average)

highest_marks = max(students.values())
lowest_marks = min(students.values())

for name, marks in students.items():
    if marks == highest_marks:
        print("Highest Scorer:", name, "with", marks, "marks")
    if marks == lowest_marks:
        print("Lowest Scorer:", name, "with", marks, "marks")

print("\nStudents scoring more than 50:")
for name, marks in students.items():
    if marks > 50:
        print(name, ":", marks)
