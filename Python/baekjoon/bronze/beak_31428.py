# 백준
# 31428번 : 엘리스 트랙 매칭
# 브론즈 4

## Cloud 트랙
## SW 엔지니어 트랙
## IOT 트랙
## AI 트랙

# 같은 트랙을 지원하는 헬로빗의 친구들은 총 몇 명이 있는지 출력

N = int(input())
fl = list(map(str, input().split()))
h = input()
count = 0

for i in range(N):
    temp = fl[i]

    if temp == h:
        count +=1

print(count)