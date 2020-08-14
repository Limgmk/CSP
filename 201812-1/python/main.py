def main():
    r, y, g = map(int, input().split())
    n = int(input())
    totalTime = 0
    for i in range(0, n):
        k, t = map(int, input().split())
        if k == 0 or k == 1:
            totalTime += t
        elif k == 2:
            totalTime += t + r

    print(f'{totalTime}')


if __name__ == '__main__':
    main()
