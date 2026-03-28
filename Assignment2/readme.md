Operating System Lab – Assignment 2

Implementation of Banker’s Algorithm for Deadlock Avoidance

Objective
This assignment focuses on implementing Banker’s Algorithm to avoid deadlock in an operating system. The goal is to understand how resource allocation is managed and how a system determines whether it is in a safe state.

Algorithm Implemented

Banker’s Algorithm
It is a deadlock avoidance algorithm.
It checks whether the system is in a safe state before allocating resources.
Ensures that all processes can complete without causing deadlock.

Input
Number of processes
Number of resources
Allocation matrix
Maximum matrix
Available resources

Output
Need Matrix
Safe or Unsafe state
Safe Sequence (if system is safe)

Formulas Used
Need = Maximum – Allocation

Analysis
Banker’s Algorithm prevents deadlock by checking system safety before allocation.
If a safe sequence exists, the system is considered safe.
If no safe sequence is found, the system is unsafe and may lead to deadlock.

Technologies Used
Python 3
Basic input/output operations

Conclusion
This assignment demonstrates how deadlocks can be avoided using Banker’s Algorithm. It ensures safe execution of processes by managing resource allocation efficiently.
