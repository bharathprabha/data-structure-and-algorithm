# Uses python3
import sys

def get_fibonacci(f, n):
    f[0] = 0
    f[1] = 1

    for i in range(2, n+1):
        f[i] = (f[i-1] + f[i-2]) % 10

    return f
def get_fibonacci_last_digit_naive(n):
    if n is 0:
        return 0
    f = [0] * 61
    f = get_fibonacci(f, 60)
    return f[n %60]


# def get_fibonacci_last_digit(n):
#     golden_ratio = (1 + math.sqrt(5)) / 2
#     val = (golden_ratio ** n - (1 - golden_ratio) ** n) / math.sqrt(5)
#     return int(val) % 10

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
