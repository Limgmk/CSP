def main():
    infos = []
    lines = []
    num1, num2 = map(int, input().split())
    for i in range(0, num1):
        x_str, y_str, type_str = input().split()
        info = {'x': int(x_str), 'y': int(y_str), 'type': type_str}
        infos.append(info)

    for i in range(0, num2):
        a_str, b_str, c_str = map(int, input().split())
        line = {'a': a_str, 'b': b_str, 'c': c_str}
        lines.append(line)

    for line in lines:
        ok = 'Yes'
        firstInfo = infos[0]
        firstRes = line['a'] + line['b'] * firstInfo['x'] + line['c'] * firstInfo['y']
        if firstRes == 0:
            ok = 'No'
        else:
            if (firstRes > 0 and firstInfo['type'] == 'A') or (firstRes < 0 and firstInfo['type'] != 'A'):
                infoType = 'A'
            else:
                infoType = 'B'
            for info in infos:
                result = line['a'] + line['b'] * info['x'] + line['c'] * info['y']
                if result == 0 or (result > 0 and info['type'] != infoType) or (result < 0 and info['type'] == infoType):
                    ok = 'No'
                    break
        print(ok)


if __name__ == '__main__':
    main()
