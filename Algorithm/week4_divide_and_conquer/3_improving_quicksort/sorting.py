# Uses python3
import sys
import random

def partition(arr, pivot):
    less, equal, greater = [], [], []
    for val in arr:
        if val  < pivot: less.append(val)
        if val == pivot: equal.append(val)
        if val  > pivot: greater.append(val)
    return less, equal, greater

def qsort(arr):
    if len(arr) <= 1: return arr
    pivot = arr[0]
    less, equal, greater = partition(arr, pivot)
    return qsort(less) + equal + qsort(greater)

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    a = qsort(a)
    for x in a:
        print(x, end=' ')
