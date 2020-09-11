def main():
    n, k = map(int, input().split())
    ws = [int(w) for w in input().split()]

    now_w = 0
    result = 0
    for w in ws:
        now_w += w
        if now_w >= k:
            now_w = 0
            result += 1
            
    if now_w != 0:
        result += 1
    print(f"{result}")
        

if __name__ == '__main__':
    main()
