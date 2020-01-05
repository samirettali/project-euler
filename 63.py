#!/usr/bin/env python3


def main():
    count = 0
    for base in range(1, 10000):
        for exp in range(1, 22):
            power = base ** exp
            if len(str(power)) == exp:
                count += 1
            if len(str(power)) > exp:
                break
    print(count)

if __name__ == '__main__':
    main()
