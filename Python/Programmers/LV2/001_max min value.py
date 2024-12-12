# 최댓값과 최솟값

# min(), max() 이용
def solution(s):
    answer = ''
    temp = []
    temp = list(map(int, s.split(' '))) ## 리스트 작업
    f = min(temp)
    l = max(temp)

    # print(f,l)
    answer = str(f) + ' ' + str(l)
    # print(temp)
    return answer
