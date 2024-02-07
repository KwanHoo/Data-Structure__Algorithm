# 알고리즘 고득점 KIT _ 해시
# 완주하지 못한 선수

#  completion : 완주 , participant : 참가자
#  문제 단순화 하기
#  문제를 간단하게 만들어보는 것이 1단계
#  해결책 1) Sorting 한 뒤에 loop를 통해 1:1 비교를 하고, 서로 다른 항목이 나온 사람이 완주하지 못한 사람임
#  해결책 2) 해시 문제니 해시 사용하는 방법
#!! 참가자 중 동명이인이 있을수 있음

#접근3 : 참고
def solution(participant, completion):
    answer = ''

    # 1. 두 list를 sorting한다
    participant.sort()
    completion.sort()

    # 2. completeion list의 len만큼 participant를 찾아서 없는 사람을 찾는다
    for i in range(len(completion)):
        if(participant[i] != completion[i]):
            return participant[i]

    # 3. 전부 다 돌아도 없을 경우에는 마지막 주자가 완주하지 못한 선수이다.
    return participant[len(participant)-1]


#접근2 동명이인 거림  : 41.7/100
def solution2(participant, completion):
    answer = ''
    flag = False
    for i in range(len(participant)):
        flag = False
        nowW = participant[i]

        for j in range(len(completion)):
            compW = completion[j]
            if nowW == compW:
                flag = True

        if flag:
            continue
        else:
            answer = participant[i]
            break
    return answer



# 접근 1 : 16/100  -> 접근 3으로 좀만더 솜보면 가능한 문제였음
def solution1(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
        else:
            continue

    return answer

