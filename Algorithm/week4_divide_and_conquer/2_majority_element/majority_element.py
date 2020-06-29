# Uses python3
import sys
from collections import Counter

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    if right % 2 is 0:
        mid = (right // 2) + 1
    else:
        mid = (right // 2) + 1
    c = Counter(a).most_common()
    if c[0][1] >= mid:
        return 1
    return -1
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
