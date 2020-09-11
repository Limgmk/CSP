def main():
    money = int(input())
    a  = int(money / 50)
    b = int((money - a * 50) / 30)
    c = int((money - a * 50 - b * 30) / 10)

    n = a * 7 + b * 4 + c
    print(f'{n}')
        

if __name__ == '__main__':
    main()
