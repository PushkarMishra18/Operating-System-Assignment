# Input
n = int(input("Enter number of processes: "))
p = []

for i in range(n):
    arrival_time = int(input(f"Arrival Time of P{i}: "))
    burst_time = int(input(f"Burst Time of P{i}: "))
    p.append([i, arrival_time, burst_time])

# SJF (Non-Preemptive, simple)
p.sort(key=lambda x: x[2])
time = 0
result = []

for i in p:
    time = max(time, i[1]) + i[2]
    completion_time = time
    turnaround_time = completion_time - i[1]
    waiting_time = turnaround_time - i[2]
    result.append([i[0], i[1], i[2], completion_time, turnaround_time, waiting_time])

# Output
print("\nSJF Table:")
print("PID\tAT\tBT\tCT\tTAT\tWT")
for row in result:
    print(*row, sep="\t")
