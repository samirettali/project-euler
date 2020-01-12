#!/usr/bin/env python3
import itertools
from math import floor, sqrt


def is_prime(n):
    if n < 2:
        return False

    if n == 2 or n == 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    for i in range(6, int(sqrt(n)) + 2, 6):
        if n % (i - 1) == 0 or n % (i + 1) == 0:
            return False

    return True


def next_prime(n):
    n += 1
    while not is_prime(n):
        n += 1
    return n


def primes_up_to(n):
    primes = []
    for i in range(2, n):
        if is_prime(i):
            primes.append(i)
    return primes


def factorize(n, primes=None):
    factors = []
    if not primes:
        primes = primes_up_to(n)
    while n > 1 and len(primes) > 0:
        p = primes[0]
        primes.remove(p)
        while n % p == 0:
            factors.append(p)
            n /= p
    return factors


def prime_factors(n, primes=None):
    result = None
    if primes:
        result = factorize(n, primes)
    else:
        result = factorize(n)
    return list(set(result))


def combinations(elements, n):
    return list(itertools.combinations(elements, n))


def unrepeated_combinations(elements, n):
    return set(combinations(elements, n))


def is_triangular(n):
    if n <= 0:
        return False
    test = (sqrt(1 + 8 * n) + 1) / 2
    return test == int(test)


def is_square(n):
    if n <= 0:
        return False
    assert n > 0
    test = sqrt(n)
    return test == int(test)


def is_pentagonal(n):
    if n <= 0:
        return False
    test = (sqrt(1 + 24 * n) + 1) / 6
    return test == int(test)


def is_hexagonal(n):
    if n <= 0:
        return False
    test = (sqrt(1 + 8 * n) + 1) / 4
    return test == int(test)


def is_heptagonal(n):
    if n <= 0:
        return False
    test = (sqrt(9 + 40 * n) + 3) / 10
    return test == int(test)


def is_octagonal(n):
    if n <= 0:
        return False
    test = (sqrt(1 + 3 * n) + 1) / 3
    return test == int(test)


def get_continued_fraction(n):
    limit = sqrt(n)
    a = int(limit)
    period = []

    if a * a != n:
        d = 1.0
        m = 0.0

        while a != 2 * int(limit):
            m = d * a - m
            d = (n - m * m) / d
            a = int((limit + m) / d)
            period.append(a)
    return [int(limit), period]


def is_permutation(s1, s2):
    return sorted(s1) == sorted(s2)
