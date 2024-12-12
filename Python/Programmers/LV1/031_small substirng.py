# 크기가 작은 부분문자열

# 1) p길이만큼 t문자열 분해 리스트 만들기
# 2) p보다 작은거 갯수 카운트
def solution(t, p):
    answer = 0

    pl = len(p)
    # print(pl)
    tlist = []
    count = 0

    for i in range(0, len(t) - pl + 1, 1):
        tlist.append(t[i:i + pl])
    # print('tlist : ', tlist)

    for j in range(len(tlist)):
        if (tlist[j] <= p):
            count += 1
    # print(count)
    answer = count
    return answer