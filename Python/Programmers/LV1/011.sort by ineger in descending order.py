# 정수 내림차순으로 배치하기

def solution(n):
    # 정수 각 자리수 분해
    ns = str(n)
    nlist = []
    for i in range(len(ns)):
        temp = ns[i]
        nlist.append(temp)

    nlist2 = sorted(nlist, reverse=True)
    temp2 = ''
    for j in range(len(nlist2)):
        temp2 += nlist2[j]
    answer = int(temp2)
    return answer


def solution2(n):
    answer = 0
    tlist= []
    temp = ''
    for i in str(n):
        tlist.append(i)
    tlist.sort(reverse = True)
    for j in tlist:
        temp +=j
    answer = int(temp)
    return answer