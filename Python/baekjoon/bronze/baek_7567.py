# 문제집) Python 배우기 (1~50)
## 7567_그릇
# 브론즈 2

## 단순 구현 문제
# vols = list(map(str, input().split()))
vols = str(input())

length = 10

if vols[0] == '(':
    flag = 'left'
else:
    flag = 'right'

for i in range(1, len(vols)):
    if vols[i] == '(' and flag == 'left':
        length += 5
        # flag = 'left'
    elif vols[i] == '(' and flag == 'right':
        length += 10
        flag = 'left'
    elif vols[i] == ')' and flag == 'left':
        length += 10
        flag = 'right'
    elif vols[i] == ')' and flag == 'right':
        length += 5
        # flag = 'right'

print(length)
