#!/usr/bin/env python3


def main():
    data = []
    f = open('datasets/p067_triangle.txt')
    for line in f:
        data.append([int(n) for n in line.split(' ')])

    while len(data) > 1:
        new_row = []
        for i in range(len(data[-2])):
            n = data[-2][i]
            left = data[-1][i]
            right = data[-1][i + 1]
            if n + left > n + right:
                new_row.append(n + left)
            else:
                new_row.append(n + right)
        data = data[:-2]
        data.append(new_row)

    print(data[0][0])


if __name__ == '__main__':
    main()
