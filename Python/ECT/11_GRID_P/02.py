# 02_곱하기 혹은 더하기

## 입력된 숫자 사이에 * or + 연산자 넣어서 가장 큰수

S = input()

first = int(S[0])
result = 0

for i in range(1,len(S)):
    # 현 숫자
    temp = int(S[i])
    if i == 1:
        if first == 0 or first == 1 or temp == 0 or temp == 1:
            result = first + temp
        else:
            result = first * temp
    else:
        if temp == 0 or temp == 1:
            result += temp
        else:
            result *= temp

print(result)


## 23.12.28 solve : 5m