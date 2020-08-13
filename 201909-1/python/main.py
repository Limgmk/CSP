def main():
    num1, num2 = map(int, input().split())
    appleTotal = 0
    maxIndex = 0
    maxNum = 0
    for i in range(0, num1):
        arrs = [int(arr_str) for arr_str in input().split()]
        delNum = 0
        for m in range(0, num2):
            delNum += arrs[m + 1]
        appleTotal += arrs[0] + delNum
        if delNum < maxNum:
            maxIndex = i
            maxNum = delNum

    print(appleTotal, maxIndex + 1, -maxNum)


if __name__ == '__main__':
    main()
