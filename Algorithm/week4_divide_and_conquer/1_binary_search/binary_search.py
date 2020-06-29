# Uses python3
import sys



def binarySearch(arr, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)
        else:
            return binarySearch(arr, mid + 1, r, x)
    else:
        return -1

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    # for x in data[n + 2:]:
    #     # # replace with the call to binary_search when implemented
    #     # print(linear_search(a, x), end = ' ')
    for x in data[n + 2:]:

        print(binarySearch(a, 0, len(a)-1, x), end = ' ')


    # while True:
    #     c = range(1, 9)
    #     t = choice(c)
    #     ar = random.sample(range(1, 100), t)
    #     ar.sort()
    #     f = choice(ar)
    #     if linear_search(ar, f + 100) == binarySearch(ar, 0, len(ar) - 1, f + 100):
    #         print("ok")
    #     else:
    #         print(t)
    #         print(ar)
    #         print(f)
    #         print(linear_search(ar, f + 100))
    #         print(binarySearch(ar, 0, len(ar) - 1, f + 100))
    #         print("error")
    #         break