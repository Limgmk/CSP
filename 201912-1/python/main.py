def judge(n):
    if n % 7 == 0:
        return False
    i = 1
    while n/i >= 1:
        if int(n/i) % 10 == 7:
            return False
        i *= 10
    return True


def main():
    total = int(input())
    counts = [0, 0, 0, 0]
    i = 0
    while total > 0:
        if judge(i + 1):
            total -= 1
        else:
            counts[i % 4] += 1
        i += 1
    for count in counts:
        print(count)


if __name__ == '__main__':
    main()

