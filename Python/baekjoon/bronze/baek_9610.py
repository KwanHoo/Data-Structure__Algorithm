# 문제집) Python 배우기 (1~50)
## 9610_사분면
# 브론즈 3

## 2차원 좌표 상의 여러 점의 좌표가 주어졌을때, 각 사부면과 축에 점이 몇개 있는지 구하는 프로그램

n = int(input())
q1c, q2c, q3c, q4c, axis = 0, 0, 0, 0, 0

for _ in range(n):
    x, y = map(int, input().split())

    ## 평면 판별
    if x == 0 or y == 0:
        axis +=1
    elif x>0 and y>0:
        q1c +=1
    elif x<0 and y>0:
        q2c +=1
    elif x<0 and y<0:
        q3c +=1
    else:
        q4c +=1

## 결과 출력
print(f'Q1: {q1c}')
print(f'Q2: {q2c}')
print(f'Q3: {q3c}')
print(f'Q4: {q4c}')
print(f'AXIS: {axis}')