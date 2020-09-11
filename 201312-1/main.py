def main():
    n = int(input())
    if (n < 1) | (n > 1000):
        return
    nums = [int(num) for num in input().split()]

    rs = [[nums[0], 1]]
    for i in range(1, len(nums)):
        num = nums[i]
        flag = 0
        for r in rs:
            if r[0] == num:
                r[1] = r[1] + 1
                flag = 1
                break
        if flag == 0:
            rs.append([num, 1])

    max = rs[0][0]
    max_num = rs[0][1]
    for i in range(1, len(rs)):
        r = rs[i]
        if r[1] > max_num | (r[1] == max_num & r[0] < max):
            max_num = r[1]
            max = r[0]

    print(f'{max}')
        

if __name__ == '__main__':
    main()
