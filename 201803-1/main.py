def main():
    nums = [int(num) for num in input().split()]

    result = 0
    if nums[0] == 1:
        result += 1
    elif nums[0] == 2:
        result += 2
    elif nums[0] == 0:
        print(f'0')
        return

    add = result
    for i in range(1, len(nums)):
        num = nums[i]
        if num == 0:
            break
        elif num == 1:
            add = 1
        elif num == 2:
            if add == 1:
                add = 2
            else:
                add += 2
        result += add

    print(f'{result}')
        

if __name__ == '__main__':
    main()
