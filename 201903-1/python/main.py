def main():
    n = int(input())
    arrs = [int(arr) for arr in input().split()]

    max = arrs[0] if arrs[0] > arrs[n - 1] else arrs[n - 1]
    min = arrs[0] if arrs[0] < arrs[n - 1] else arrs[n - 1]

    if n % 2 == 1:
        median = arrs[int((n-1)/2)]
    else:
        median = (arrs[int(n/2 - 1)] + arrs[int(n/2)])/2
        median = int(median) if median - int(median) != 0.5 else median

    print(f'{max} {median} {min}')


if __name__ == '__main__':
    main()
