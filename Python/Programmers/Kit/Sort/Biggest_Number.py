# 알고리즘 고득점 KIT _ 정렬
# 가장 큰 수

## 1. 정렬을 내림차순으로
## 2. 나열

def solution(numbers):
    answer = ''

    numbers = list(map(str, numbers))  # string으로 바꾸어서 비교
    numbers.sort(key=lambda x: x * 3, reverse=True)  # 3번씩 반복하면 붙였을때 큰수 찾기 가능

    for i in numbers:  # 정렬된 리스트를 answer에 순서대로 더해줌
        answer += i

    return str(int(answer))


### 참고
#  lambda x: x * 3는 각 요소를 3번 반복시키는 역할
#  예를 들어, [1, 2, 3]이라는 리스트가 있을 때, 정렬 후에는 [333, 222, 111]이 될 것입니다.