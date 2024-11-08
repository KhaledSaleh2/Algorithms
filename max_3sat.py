import sys
import random

num_variables = int(sys.stdin.readline())
variables = [0] * num_variables
num_clauses = int(sys.stdin.readline())
clauses = []
for i in range(num_clauses):
    new_clause = sys.stdin.readline().split()
    clauses.append(new_clause)
num_satisfied = 0
goal = num_clauses * 7 / 8
while num_satisfied < goal:
    for i in range(num_variables):
        variables[i] = random.choice([-1,1])
    num_satisfied = 0
    for clause in clauses:
        for val in clause:
            num = int(val)
            index = abs(num) - 1
            if num <= variables[index] < 0 or num >= variables[index] > 0:
                num_satisfied += 1
                break
for val in variables:
    print(val, end=' ')