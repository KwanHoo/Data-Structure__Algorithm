# 최솟값 만들기

# * 배열에서 두수 뽑아 곱함
# * 두수 곱한 값 누적하여 더함
# * 최종 누적값이 최소가 되게..
## 하나 내림차순, 하나 오름차순
def solution(A, B):
    answer = 0
    A.sort(reverse=True)
    B.sort()
    temp = []
    for i in range(len(A)):
        temp2 = A[i] * B[i]
        temp.append(temp2)

    # print(temp)
    answer = sum(temp)
    return answer