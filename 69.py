#!/usr/bin/env python3
from library import next_prime


def main():
    limit = 1000000
    n = 1
    prime = 2

    while n * prime <= limit:
        n *= prime
        prime = next_prime(prime)

    print(n)


if __name__ == '__main__':
    main()
