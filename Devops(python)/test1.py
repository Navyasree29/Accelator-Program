'''1.Multi-Server Health Aggregator 
Problem Statement: 
You joined as a DevOps Intern at a mid-sized company. Your task is to help the Operations team by 
automating a health check report of all their servers. 
They want to input the number of servers, and for each server: 
 Server name 
 CPU usage (%) 
 Memory usage (%) 
 Disk usage (%) 
Write a Python program that: 
 Checks if any metric exceeds thresholds (CPU > 85%, Memory > 80%, Disk > 90%). 
 Prints warnings for unhealthy servers. 
 Displays the total count of unhealthy servers. 
Sample input and output: 
Enter the number of servers: 3 
Enter details for server 1: 
Server name: web 
CPU usage (%): 65 
Memory usage (%): 86 
Disk usage (%): 75 
Enter details for server 2: 
Server name: cache 
CPU usage (%): 86 
Memory usage (%): 75 
Disk usage (%): 50 
Enter details for server 3: 
Server name: jail 
CPU usage (%): 92 
Memory usage (%): 81 
Disk usage (%): 76 
Server web is unhealthy: Memory high'''

n=int(input("Enter the number of servers: "))
servers=[]
for i in range(n):
    print(f"Enter details for server {i+1}:")
    s=input("Server name: ")
    c=int(input("CPU usage (%): "))
    m=int(input("Memory usage (%): "))
    d=int(input("Disk usage (%): "))
    servers.append({"server": s, "cpu": c, "memory": m, "disk": d})
count=0
for x in servers: 
    warnings = [] 
    if x["cpu"] > 85: 
        warnings.append("CPU high") 
    if x["memory"] > 80: 
        warnings.append("Memory high") 
    if x["disk"] > 90: 
        warnings.append("Disk high") 
 
    if warnings: 
        print(f"\nServer {x['server']} is unhealthy: {', '.join(warnings)}") 
        count += 1 
 
print(f"\nTotal unhealthy servers: {count}")

