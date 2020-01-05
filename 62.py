#!/usr/bin/env python3


def main():
    cubes = {}
    found = False
    n = 1
    while not found:
        perm = ''.join(c for c in sorted(str(n ** 3)))
        if perm in cubes:
            cubes[perm].append(n)
            if len(cubes[perm]) == 5:
                print(min(cubes[perm]) ** 3)
                found = True
        else:
            cubes[perm] = [n]
        n += 1


if __name__ == '__main__':
    main()
