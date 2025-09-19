'''3.Resource Monitoring with Alerts 
Mode Problem Statement: 
Your DevOps lead asks you to build a monitoring simulation tool. 
The user will input how many resource checks they want to simulate. 
For each check, the CPU and Memory usage will be entered. 
Write a Python program that: 
 Alerts if CPU usage exceeds 85% or Memory exceeds 80%.

Sample input and output: 
Enter number of resource checks: 3 
CPU usage at check 1 (%): 65 
Memory usage at check 1 (%): 85 
CPU usage at check 2 (%): 76 
Memory usage at check 2 (%): 87 
CPU usage at check 3 (%): 59 
Memory usage at check 3 (%): 65 
Alert at check 1: CPU 65%, Memory 85% 
Alert at check 2: CPU 76%, Memory 87% 
 
Enter number of resource checks: 2 
CPU usage at check 1 (%): 56 
Memory usage at check 1 (%): 75 
CPU usage at check 2 (%): 75 
Memory usage at check 2 (%): 78
'''

num_checks = int(input("Enter number of resource checks: ")) 
cpu_usages = [] 
memory_usages = [] 
 
for i in range(num_checks): 
    cpu = int(input(f"CPU usage at check {i+1} (%): ")) 
    memory = int(input(f"Memory usage at check {i+1} (%): ")) 
    cpu_usages.append(cpu) 
    memory_usages.append(memory) 
 
for i in range(num_checks): 
    if cpu_usages[i] > 85 or memory_usages[i] > 80: 
        print(f"Alert at check {i+1}: CPU {cpu_usages[i]}%, Memory {memory_usages[i]}%") 
 

 
