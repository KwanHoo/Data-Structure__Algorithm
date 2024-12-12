# 약수의 개수와 덧셈

#약수의 개수
def solution(left, right):
    answer = 0

    akc = 0
    for i in range(left, right+1):
        temp = getMyDivisor(i)
        # print(temp)
        if (len(temp) % 2 ==0):
            akc += i
        else:
            akc -= i
    answer = akc
    return answer

## 약수구하는 함수
def getMyDivisor(n):

    divisorsList = []

    for i in range(1, n + 1):
        if (n % i == 0) :
            divisorsList.append(i)

    return divisorsList