#Uses python3

import sys

def get_max(num_one, num_two):
    temp_a = int(str(num_one) + str(num_two))
    temp_b = int(str(num_two) + str(num_one))
    if temp_a >= temp_b:
        return num_one
    else:
        return num_two

def get_max_salary(numbers):
    n = len(numbers)
    temp_n = len(numbers)
    result = ""
    while temp_n != 0:
        max_num = numbers[0]
        temp_index = 0
        for i in range(0, n):
            max_num = get_max(max_num, numbers[i])
            if max_num == numbers[i]:
                temp_index = i
        result += str(max_num)
        numbers[temp_index] = 0
        temp_n -= 1
    return result

# def largest_number(a):
#     #write your code here
#     res = ""
#     for x in a:
#         res += x
#     return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(get_max_salary(a))
    
