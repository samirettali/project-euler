#!/usr/bin/env python3
from sys import argv


def main():
    cubes = {}
    limit = 5
    smallest = []
    for n in range(10000):
        cube = n ** 3
        cubes[cube] = n

    for c1 in cubes:
        r1 = cubes[c1]
        found = [c1]
        s1 = ''.join(c for c in sorted(str(c1)))
        for c2 in cubes:
            r2 = cubes[c2]
            s2 = ''.join(c for c in sorted(str(c2)))
            if s1 == s2 and r1 != r2:
                found.append(c2)
        if len(found) == limit and (not smallest or min(found) < min(smallest)):
            smallest = found
    print(min(smallest))

if __name__ == '__main__':
    main()
