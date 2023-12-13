# 문제집) Python 배우기 (1~50)
## 2675_문자열 반복
# 브론즈 2

T = int(input())

for tc in range(T):
    N, words = list(map(str, input().split()))

    Ni = int(N)
    # print(words)
    result = ''
    for i in range(len(words)):
        temp = words[i]
        result += temp * Ni

    print(result)   ## 결과 출력