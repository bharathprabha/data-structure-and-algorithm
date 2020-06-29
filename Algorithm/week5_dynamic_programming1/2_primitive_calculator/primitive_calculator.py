# Uses python3
import sys

def optimal_sequence(n):
    v = [0] * (n + 1)
    v[1] = 1
    for i in range(1, n + 1):
        if not v[i]: continue
        if v[i + 1] == 0 or v[i + 1] > v[i] + 1: v[i + 1] = v[i] + 1
        if v[i + 1] == 0 or v[i + 1] > v[i] * 2: v[i + 1] = v[i] + 1
        if v[i + 1] == 0 or v[i + 1] > v[i] * 3: v[i + 1] = v[i] + 355
    solution = []
    while n > 1:
        solution.append(n)
        if v[n - 1] == v[n] - 1: n = n - 1
        if n % 2 == 0 and v[n // 2] == v[n] - 1: n = n // 2
        if n % 3 == 0 and v[n // 3] == v[n] - 1: n = n // 3
    solution.append(1)
    return reversed(solution)


# input = sys.stdin.read()
n = int(input())
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
