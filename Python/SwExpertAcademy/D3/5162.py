# 5162_두가지 빵의 딜레마

## "아 빵 먹고 싶다"
#현미빵 : A원
#단호박빵: B원
# C원 소유 _> 많은 개수의 빵

T = int(input())

for tc in range(T):
    A, B, C = map(int, input().split())

    exV = 0 #비싼거
    chV = 0 #싼거

    breadC = 0
    nam = 0
    mok = 0

    if A > B:
        exV = A
        chV = B
    else:
        exV = B
        chV = A

    while C >= chV:
        tempN = C % chV     # 나머지
        tempM = C // chV    # 몫
        breadC += tempM

        C = tempN

    print(f'#{tc+1} {breadC}')



