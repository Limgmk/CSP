def main():
    n = int(input())
    nums = sorted([int(num) for num in input().split()], reverse=False)

    result = -1
    t1, t2 = 0, 0
    if n % 2 == 1:
        t1 = nums[int(n/2)]
        t2 = t1
    else:
        t1 = nums[int(n/2) - 1]
        t2 = nums[int(n/2)]

    x, y = 0, 0
    for x in range(0, len(nums)):
        if nums[x] == t1:
            break
    for y in range(0, len(nums)):
        if nums[len(nums) - y - 1] == t2:
            break

    if x == y:
        if t1 == t2:
            result = t1
    elif x - y == 1:
        if t1 != t2:
            result = t1
    elif x - y == -1:
        if t1 != t2:
            result = t2
    print(f'{result}')


if __name__ == '__main__':
    main()
