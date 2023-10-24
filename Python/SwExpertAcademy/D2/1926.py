# 1926 간단한 369게임

# 3,6,9 가 들어간 숫자가 들어간 만큼 박수

# "-" 박수한번, "--" 박수두번
## 3 6 9
## 36 39  63 69  93 96
## 369 396   639 693   936 963

## 접근 : in 사용
# N = int(input())
# result = ""
# t = ["369", "396", "639", "693", "936", "963"]
# s = ["36", "39", "63", "69", "93", "96"]
# for i in range(1, N+1):
#     if str(i) in t:
#         result = result + "--- "
#     elif str(i) in s:
#         result = result + "-- "
#     elif str(i) in "3":
#         result = result + "- "
#     elif str(i) in "6":
#         result = result + "- "
#     elif str(i) in "9":
#         result = result + "- "
#     else:
#         result = result + str(i) + " "
#
# print(result)
## -> 문제 in 배열로 모든 경우의 수를 넣어주어야됨 235 이런거는 그냥 출력되버림


## solve idea : count 함수 이용
N = int(input())
for i in range(1, N+1):

    i = str(i)
    clap = i.count('3') + i.count('6') + i.count('9')

    if clap == 0:
        print(i, end=' ')
    else:
        print("-" * clap, end=' ')


## 리스트 이용 풀이
N = int(input())
clap = ['3', '6', '9']

for i in range(1, N+1):
    count = 0
    for j in str(i): ## 숫자 하나씩 뽑음
        if j in clap:
            count += 1 ## 3, 6, 9 들어갈 때 마다 카운트 1씩 증가시킴
    if count > 0:
        i = '-' * count
    print(i, end=' ')