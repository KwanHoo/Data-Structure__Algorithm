# 문제집) Python 배우기 (1~50)
## 3009_네 번째 점
# 브론즈 3

## 세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해 네번째 점 찾는 프로그램

T = 3
flist = []
slist = []

for _ in range(T):
    f, s = map(int, input().split())

    flist.append(f)
    slist.append(s)
flist.sort()
slist.sort()


## 리스트 중간값으로 나머지 점 좌표 판별
if flist[1] == flist[0]:
    resultf = flist[2]
elif flist[1] == flist[2]:
    resultf = flist[0]

if slist[1] == slist[0]:
    results = slist[2]
elif slist[1] == slist[2]:
    results = slist[0]

## 결과 좌표 출력
print(resultf, results)