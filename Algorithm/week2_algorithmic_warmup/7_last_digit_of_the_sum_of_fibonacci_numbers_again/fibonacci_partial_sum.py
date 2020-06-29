# Uses python3
import sys

# def fibonacci_partial_sum_naive(from_, to):
#     sum = 0
#
#     current = 0
#     next  = 1
#
#     for i in range(to + 1):
#         if i >= from_:
#             sum += current
#
#         current, next = next, current + next
#
#     return sum % 10

def pisanoPeriod(m):
    previous, current = 0, 1
    for i in range(0, m * m):
        previous, current \
            = current, (previous + current) % m

        # A Pisano Period starts with 01
        if (previous == 0 and current == 1):
            return i + 1

def get_fibonacci_huge(n, m):
    pisano_period = pisanoPeriod(m)

    n = n % pisano_period

    previous, current = 0, 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    for i in range(n - 1):
        previous, current \
            = current, previous + current

    return (current % m)

def fibonacci_partial_sum(from_, to):
    ataas = get_fibonacci_huge(to + 2, 10) - get_fibonacci_huge(from_ + 1, 10)
    if ataas < 0:
        return 10 + ataas
    elif ataas > 9:
        return ataas % 10
    else:
        return ataas


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum(from_, to))