'''5.Automated Log Cleanup 
Problem Statement: 
You’re developing an automated cleanup utility for logs. 
The user will enter the number of log files manually, along with file names that have timestamps 
embedded. 
Files older than 6 months should be marked for deletion. 
Write a Python program that: 
 Processes user-entered file names. 
 Prints which files would be deleted and which will be kept. 
 
 
Sample input and output: 
Enter number of log files: 3 
Enter file name 1 (format: 'app_log_YYYYMMDD.log'): app_log_20250912.log 
Enter file name 2 (format: 'app_log_YYYYMMDD.log'): app_log_20231203.log 
Enter file name 3 (format: 'app_log_YYYYMMDD.log'): app_log_20241205.log 
Deleted files: ['app_log_20231203.log', 'app_log_20241205.log'] 
Remaining files: ['app_log_20250912.log'] 
 
'''
from datetime import datetime, timedelta 
 
num_files = int(input("Enter number of log files: ")) 
files = [] 
 
for i in range(num_files): 
    file = input(f"Enter file name {i+1} (format: 'app_log_YYYYMMDD.log'): ") 
    files.append(file) 
 
today = datetime.today() 
threshold_date = today - timedelta(days=180) 
 
deleted_files = [] 
remaining_files = [] 
 
for file in files: 
    date_str = file.split('_')[2].split('.')[0]  # Extract YYYYMMDD 
    file_date = datetime.strptime(date_str, "%Y%m%d") 
 
    if file_date < threshold_date: 
        deleted_files.append(file) 
    else: 
        remaining_files.append(file) 
 
print("Deleted files:", deleted_files) 
print("Remaining files:", remaining_files)