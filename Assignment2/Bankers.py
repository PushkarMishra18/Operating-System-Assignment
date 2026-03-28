# Input
n = int(input("Processes: "))
m = int(input("Resources: "))

allocation = []
maximum = []

print("Enter Allocation:")
for i in range(n):
    allocation.append(list(map(int, input().split())))

print("Enter Maximum:")
for i in range(n):
    maximum.append(list(map(int, input().split())))

available = list(map(int, input("Enter Available: ").split()))

# Need
need = [[maximum[i][j] - allocation[i][j] for j in range(m)] for i in range(n)]

print("\nNeed Matrix:")
for i in range(n):
    print(f"P{i} ->", *need[i])

# Safety
finish = [0]*n
safe_sequence = []
work = available.copy()

for _ in range(n):
    for i in range(n):
        if not finish[i] and all(need[i][j] <= work[j] for j in range(m)):
            work = [work[j] + allocation[i][j] for j in range(m)]
            safe_sequence.append(i)
            finish[i] = 1

# Output
print("\nResult:")
if len(safe_sequence) == n:
    print("System is SAFE")
    print("Safe Sequence:", " -> ".join(f"P{i}" for i in safe_sequence))
else:
    print("System is UNSAFE")
