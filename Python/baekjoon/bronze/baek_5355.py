# 문제집) Python 배우기 (1~50)
## 5355_화성 수학
# 브론즈 2

## @ = *3
## % = +5
## # = -7


T = int(input())

for tc in range(T):
    words = list(map(str, input().split()))

    fn = float(words[0])
    result = 0
    for i in range(1, len(words)):
        temp = words[i]

        if temp == '@':
            fn = fn * 3
        elif temp == '%':
            fn = fn + 5
        elif temp == '#':
            fn = fn - 7

    print(f'{fn:.2f}')  ## 소수점 자리 조절 가능
