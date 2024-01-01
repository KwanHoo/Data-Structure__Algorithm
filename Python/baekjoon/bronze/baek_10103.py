# 문제집) Python 배우기 (1~50)
## 10103_주사위 게임
# 브론즈 3

## 100점으로 둘다 시작
## 낮은 숫자가 나온 사람은 상대편 주사위에 나온 숫자만큼 점수를 잃게됨
#! 두 사람의 주사위가 같은 숫자가 나온 경우에는 점수 잃지 않음

T = int(input())
As = 100
Bs = 100

for _ in range(T):
    A, B = map(int,input().split())

    if A == B:
        continue
    elif A > B:
        temp = A
        Bs -= temp
    elif A < B:
        temp = B
        As -= temp

print(As)
print(Bs)
