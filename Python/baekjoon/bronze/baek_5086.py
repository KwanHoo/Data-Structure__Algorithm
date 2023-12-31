# 문제집) Python 배우기 (1~50)
## 5086_배수와 약수
# 브론즈 3

## 두 수가 주어졌을 때, 어떤 관계인지 구하는 프로그램
### 첫 번째 숫자가 두 번째 숫자의 약수이다.                 : factor
### 첫 번째 숫자가 두 번째 숫자의 배수이다.                 : multiple
### 첫 번째 숫자가 두 번째 숫자의 약수와 배수 모두 아니다.    : neither

endbreak = True

while endbreak:
    fst, scd = map(int, input().split())

    if fst == 0 and scd ==0:
        endbreak = False
        break

    ## 판별
    if fst >= scd:
        big = fst
        sml = scd
    else:
        big = scd
        sml = fst

    nam = big % sml

    if nam == 0:
        if big == fst:
            result = 'multiple'
        else:
            result = 'factor'
    else:
        result = 'neither'

    print(result)