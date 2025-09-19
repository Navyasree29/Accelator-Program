'''2.Log File Analyzer 
 Problem Statement: 
During your internship, you’re asked to analyze the system logs. 
The system admin will input a number of log entries manually in the format: 
2025-09-13 10:15:00 INFO System started 
Write a Python program that: 
 Accepts a number of log lines from the user. 
 Counts the number of INFO, WARNING, and ERROR logs. 
 Displays the most frequent log level. 
 
Sample input and output: 
Enter number of log entries: 3 
Enter log entry 1 (e.g., '2025-09-13 10:15:00 INFO System started'): 2025-09-14 11:50:25 WARNING 
high memory usage 
Enter log entry 2 (e.g., '2025-09-13 10:15:00 INFO System started'): 2025-09-14 10:35:30 INFO 
system stopped 
Enter log entry 3 (e.g., '2025-09-13 10:15:00 INFO System started'): 2025-09-14 09:36:25 INFO User 
login 
WARNING: 1 
INFO: 2 
Most frequent log level: INFO 
 

'''

from collections import Counter 
 
num_logs = int(input("Enter number of log entries: ")) 
log_entries = [] 
 
for i in range(num_logs): 
    log = input(f"Enter log entry {i+1} (e.g., '2025-09-13 10:15:00 INFO System started'): ") 
    log_entries.append(log) 
 
levels = [] 
 
for entry in log_entries: 
    parts = entry.split() 
    levels.append(parts[2]) 
 
counter = Counter(levels) 
 
for level, count in counter.items(): 
    print(f"{level}: {count}") 
 
most_common = counter.most_common(1)[0][0] 
print(f"Most frequent log level: {most_common}")