#!/usr/bin/env python3
import library


def first_two(n):
    return int(n / 100)


def last_two(n):
    return int(n % 100)


def find_chain(d, chain):
    if len(chain) == 6:
        return chain
    last = chain[-1]
    for base, n in d[last]:
        if (base, n) in d:
            valid = True
            for b, m in chain:
                if base == b or n == m:
                    valid = False
            if valid:
                if len(chain) == 5 and last_two(n) != first_two(chain[0][1]):
                    return
                new_chain = chain.copy()
                new_chain.append((base, n))
                result = find_chain(d, new_chain)
                if result and len(result) == 6:
                    return result
    return None


def main():
    numbers = [[] for i in range(6)]
    triangulars = set()
    squares = set()
    pentagonals = set()
    hexagonals = set()
    heptagonals = set()
    octagonals = set()
    d = {}

    for i in range(1000, 10000):
        if library.is_triangular(i):
            numbers[0].append(i)
        if library.is_square(i):
            numbers[1].append(i)
        if library.is_pentagonal(i):
            numbers[2].append(i)
        if library.is_hexagonal(i):
            numbers[3].append(i)
        if library.is_heptagonal(i):
            numbers[4].append(i)
        if library.is_octagonal(i):
            numbers[5].append(i)


    for i in range(6):
        for n in numbers[i]:
            for j in range(6):
                for m in numbers[j]:
                    if last_two(n) == first_two(m):
                        if not (i, n) in d:
                            d[(i, n)] = [(j, m)]
                        else:
                            d[(i, n)].append((j, m))

    for base, n in d:
        chain = find_chain(d, [(base, n)])
        if chain:
            s = 0
            for b, n in chain:
                s += n
            print(s)
            return


if __name__ == '__main__':
    main()
