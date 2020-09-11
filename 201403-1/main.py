def main():
    n = int(input())
    nums = [int(num) for num in input().split()]
    count = 0
    for num1 in nums:
        for num2 in nums:
            if num1 + num2 == 0:
                count += 1
                break
    total = int(count/2)
    print(f'{total}')


if __name__ == '__main__':
    main()
