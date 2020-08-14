def main():
    r, y, g = map(int, input().split())
    n = int(input())
    total_time = 0
    for i in range(0, n):
        k, t = map(int, input().split())
        if k == 0 or k == 1:
            total_time += t
        elif k == 2:
            total_time += t + r

    print(f'{total_time}')


if __name__ == '__main__':
    main()
