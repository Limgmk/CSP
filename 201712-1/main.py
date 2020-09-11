def main():
    n = int(input())
    nums = [int(num) for num in input().split()]

    result = nums[0] - nums[1]
    if result < 0:
        result = 0 - result
    for i in range(0, len(nums) - 1):
        x = nums[i]
        for m in range(i + 1, len(nums)):
            y = nums[m]
            cha = x - y
            if cha < 0:
                cha = 0 - cha
            if cha < result:
                result = cha

    print(f'{result}')
        

if __name__ == '__main__':
    main()
