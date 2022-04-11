## 백준 2750
## 수 정렬하기
## 구현, 정렬

import sys

data = []
N = int(input())
for i in range(N):
    temp = sys.stdin.readline().rstrip()  # rstrip() 개행 제거
    data.append(int(temp)) ##! data.append(temp) 는 반례에 걸림

# 방식 1_1)
data.sort()

# print(*data, sep="\n") ## 1-2)프린트 다른 방법
for i in data:
    print(i)
## 반례1)
# 2
# 9
# 10
## 출력
# 10
# 9

##* 입력받은 값을 문자열로 저장하고 정렬했기 때문에 발생하는 오답
##* 문자열끼리 비교는 첫 번째 글자부터 순서대로 비교하기에 10보다 9가 더 큰 문자열임
##! int로 변환해주기