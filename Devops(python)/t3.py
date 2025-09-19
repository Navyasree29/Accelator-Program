"""Task 3: Simple Expense Tracker 
�
� Problem: 
 Assume a user records their expenses for 7 days (one week). 
 Input daily expenses and store them in a list. 
 Perform the following: 
1. Print the total and average expense. 
2. Store the results in a dictionary like: 
3. {"Total": 3500, "Average": 500} 
4. Assign the highest and lowest expense to two separate variables using multiple 
assignment. 
5. Print them clearly. 
�
� Concepts Used: 
 Numbers (sum, average) 
 Lists (store daily expenses) 
 Dictionary (summary report) 
 Multiple Assignment (highest, lowest)
"""

expenses = []
for i in range(7):
    amount = float(input("Enter expense for day {}: ".format(i+1)))
    expenses.append(amount)

total = sum(expenses)
average = total / 7
report = {"Total": total, "Average": average}
print("Report:", report)

highest, lowest = max(expenses), min(expenses)
print("Highest Expense:", highest)
print("Lowest Expense:", lowest)
