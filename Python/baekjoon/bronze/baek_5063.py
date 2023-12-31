# 문제집) Python 배우기 (1~50)
## 5063_TGN
# 브론즈 3

## TGN : Tennager Game Network -> Temporary Group Name

## 광고 효과가 주어졌을때 광고를 해야할지 말아야할지 결정하는 프로그램

## r 광고를 하지 않았을때 수익
## e 광고를 했을 때 수익
## c 광고 비용

#식1 : result = e - c :광고를 했을때 수익
#식2 : result = r : 광고 안했을때 수익

### 광고를 해야하면 advertise
### 하지 않아야 하면 do not advertise
### 광고를 해도 수익이 차이가 없다면 does not matter

N = int(input())

for _ in range(N):
    r, e, c = list(map(int,input().split()))

    result1 = e-c

    if r == result1:
        print('does not matter')
    elif r > result1:
        print('do not advertise')
    elif r < result1:
        print('advertise')