# Uses python3
import sys

# def fibonacci_sum_naive(n):
#     if n <= 1:
#         return n
#
#     previous = 0
#     current  = 1
#     sum      = 1
#
#     for _ in range(n - 1):
#         previous, current = current, previous + current
#         sum += current
#
#     return sum % 10

def getPP(m):
    pre, cur = 0, 1
    for i in range(0, m * m):
        pre, cur = cur, (pre + cur) % m
        if (pre == 0 and cur == 1):
            return i + 1


def get_fibonacci(n):
    pp = getPP(10)
    n = n % pp
    pre = 0
    cur = 1

    for _ in range(n - 1):
        pre, cur = cur, pre + cur
    return cur
def fibonacci_sum_last_digit(a):
    if a is 0:
        return 0
    return (get_fibonacci(a+2) - 1) % 10

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_last_digit(n))
