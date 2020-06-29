# Uses python3
import sys

def get_change(V):
    if V is 0:
        return 0
    deno = [1, 5, 10]
    n = len(deno)
    ans = 0
    i = n - 1
    while (i >= 0):
        while (V >= deno[i]):
            V -= deno[i]
            ans += 1
        i -= 1
    return ans

if __name__ == '__main__':
    # m = int(sys.stdin.read())
    m = int(input())
    print(get_change(m))
