#!/usr/bin/env python3
from math import gcd

def main():
    start = 2 / 5
    end = 3 / 7
    maximum = 2 / 5
    solution = None

    for d in range(1000000, 0, -1):
        s = int(d * start) + 1
        e = int(d * end) + 1
        for n in range(s, e + 1):
            result = n / d
            if gcd(n, d) == 1 and result > start and result < end:
                start = result
                solution = n

    print(solution)


if __name__ == '__main__':
    main()
