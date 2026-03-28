Operating System Lab – Assignment 1

Implementation and Analysis of CPU Scheduling Algorithms (FCFS & SJF)

Objective
This assignment focuses on implementing basic CPU scheduling algorithms and analyzing their performance. The goal is to understand how processes are scheduled and how different algorithms affect execution time.

Algorithms Implemented

1. First Come First Serve (FCFS)
   Processes are executed in the order of their arrival time.
   It is a non-preemptive scheduling algorithm.
   Simple to implement but may result in higher waiting time.

2. Shortest Job First (SJF)
   Process with the smallest burst time is executed first.
   Also non-preemptive in this implementation.
   Provides better average waiting time compared to FCFS.

Input
Number of processes
Arrival Time (AT) for each process
Burst Time (BT) for each process

Output
Table showing:
Process ID (PID)
Arrival Time (AT)
Burst Time (BT)
Completion Time (CT)
Turnaround Time (TAT)
Waiting Time (WT)

Formulas Used
Turnaround Time (TAT) = Completion Time – Arrival Time
Waiting Time (WT) = Turnaround Time – Burst Time

Analysis
FCFS is simple but can lead to longer waiting times (convoy effect).
SJF improves performance by minimizing average waiting time.
SJF is generally more efficient than FCFS when burst times are known.

Technologies Used
Python 3
Basic input/output operations

Conclusion
This assignment demonstrates how CPU scheduling algorithms impact system performance. Among the two, SJF provides better efficiency, while FCFS remains easier to implement.
