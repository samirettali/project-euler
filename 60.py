#!/usr/bin/env python3
import time
from library import primes_sieve, is_prime, combinations


def concat_numbers(n, m):
    return int(str(n) + str(m))


def find_concatenables(n, primes):
    c = set()
    for p in primes[primes.index(n) + 1:]:
        if is_prime(concat_numbers(n, p)) and is_prime(concat_numbers(p, n)):
            c.add(p)
    return c


def find_intersection(current_set, primes, concatenables, length):
    if len(current_set) == length:
        return current_set

    for p in primes:
        if p not in concatenables:
            concatenables[p] = find_concatenables(p, primes)
        valid = True
        for n, m in combinations(current_set + [p], 2):
            if (m not in concatenables or n not in concatenables[m]) and (n not in concatenables or m not in concatenables[n]):
                valid = False
                break
        if valid:
            new_set = find_intersection(current_set + [p], primes, concatenables, length)
            if new_set:
                return new_set
    return None


def main():
    primes = primes_sieve(10000)
    concatenables = dict()
    intersection = None
    while not intersection:
        intersection = find_intersection([primes.pop(0)], primes, concatenables, 5)
    print(sum(intersection))


if __name__ == '__main__':
    main()
