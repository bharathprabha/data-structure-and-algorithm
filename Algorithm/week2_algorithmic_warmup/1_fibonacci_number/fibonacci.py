
# def calc_fib(n):
#     golden_ratio = (1 + math.sqrt(5)) / 2
#     val = (golden_ratio ** n - (1 - golden_ratio) ** n) / math.sqrt(5)
#     return int(round(val))

def calc_fib(n):
    if n is 0:
        return 0
    a = [0 for _ in range(n+1)]
    a[0] = 0
    a[1] = 1
    for i in range(2,n+1):
        a[i] = a[i-1] + a[i-2]
    return a[-1]

n = int(input())
print(calc_fib(n))
