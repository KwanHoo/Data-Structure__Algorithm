# 알고리즘 고득점 KIT _ 해시
# 의상

#   경우의 수 문제
#   해결책 1) 해시를 통해 각 type 별로 가짓수를 계산하고 총 경우의 수를 산출함
#   key : 옷의 종류, Value : 옷 종류의 가짓수(count)

def solution(clothes):
    answer = 0
    hashmap = {}

    for i in range(len(clothes)):
        keyx = clothes[i][1]
        # 해쉬맵에 키값 기존재 안하는 경우
        if keyx not in hashmap:
            hashmap[keyx] = 1
        else:                       # 기존재 하는 경우
            temp = hashmap[keyx]    # 벨류값
            hashmap[keyx] = temp +1
    # print(hashmap)#	{'headgear': 2, 'eyewear': 1}

    ## 해쉬맵 경우의수  3*2 -1 (아무것도 입지않는경우 1개 빼주기)
    result = 1
    for j in hashmap:
        result *= hashmap[j]+1
        # print(result, hashmap[j])

    answer = result-1

    return answer

# 2024.02.08 : 16m