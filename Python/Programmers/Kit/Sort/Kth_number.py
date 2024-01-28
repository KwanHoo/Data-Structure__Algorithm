# 알고리즘 고득점 KIT _ 정렬
# K번째수

## array : 입력값
## commands

def solution(array, commands):
    answer = []
    for nc in range(len(commands)):
        nowc = commands[nc]
        I, J, K = nowc

        # print(I,J,K)
        ## 슬라이싱
        sl = array[I-1:J]
        # print(sl)
        ## 정렬
        sl.sort()
        result = sl[K-1]
        answer.append(result)

    return answer