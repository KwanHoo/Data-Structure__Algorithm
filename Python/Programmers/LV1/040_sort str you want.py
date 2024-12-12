# 문자열 내 마음대로 정렬하기

## n 이 인덱스
## 인덱스 문자 정렬

# * 문자열 앞에 인덱스 문자 추가 -> GOOD
def solution(strings, n):
    answer = []
    for i in strings:
        answer.append(i[n] + i)
    print(answer)
    answer.sort()
    print(answer)
    return [i[1:] for i in answer] ## return 리스트 슬라이싱


# * 추가 참고 풀이
def solution4(strings, n):
    strings.sort()
    print(strings)
    return sorted(strings, key=lambda x: x[n])
    ## 람다 활용 key를 n번째로 sorted

