# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    numRefills = 0
    currentPosition = 0
    crTr = 0
    t = len(stops) - 1
    lastPosition = currentPosition
    while currentPosition <= t:
        lastPosition = currentPosition
        if currentPosition <= t:
            while currentPosition <= t and stops[currentPosition] - crTr <= tank:
                currentPosition += 1
        crTr = stops[currentPosition]
        if currentPosition is lastPosition:
            return -1
        numRefills += 1
    return numRefills

if __name__ == '__main__':
    # d, m, _, *stops = map(int, sys.stdin.read().split())
    # print(compute_min_refills(d, m, stops))
    print(compute_min_refills(950 , 400 , [200, 375, 550, 750] ))

