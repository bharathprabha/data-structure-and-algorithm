
# def max_pairwise_product(numbers):
#     n = len(numbers)
#     max_product = 0
#     for first in range(n):
#         for second in range(first + 1, n):
#             max_product = max(max_product,
#                 numbers[first] * numbers[second])
#
#     return max_product

def maxPair(ar):
    maxIndex1 = -1
    n = len(ar)
    for i in range(n):
        if maxIndex1 is -1 or ar[i] > ar[maxIndex1]:
            maxIndex1 = i
    maxIndex2 =-1
    for i in range(n):
        if i != maxIndex1 and (maxIndex2 is -1 or ar[i] > ar[maxIndex2]):
            maxIndex2 = i
    return ar[maxIndex1] * ar[maxIndex2]


if __name__ == '__main__':

    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(maxPair(input_numbers))

