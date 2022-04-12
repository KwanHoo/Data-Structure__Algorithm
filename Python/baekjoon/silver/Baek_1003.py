##* 백준 1003번
##* 피보나치 함수
## 다이나믹 프로그래밍

##* 재귀 함수 사용한 피보
def refibo(num):
    global zeroC
    global oneC

    if num == 0:
        zeroC += 1
        return 0
    elif num == 1:
        oneC += 1
        return 1
    else:
        return refibo(num-1) + refibo(num-2)


##* 동적 프로그래밍 피보
def dpfibo(num):
    N_1 = 1
    N_2 = 1

    if num == 0:
        return 0
    elif num == 1:
        return 1
    elif num == 2:
        return 1
    
    for i in range(3, num+1):
        N_3 = N_1 + N_2
        N_2 = N_1
        N_1 = N_3

    return N_3


##* 제출 코드
def fibonacci(num):
    length = len(zero)
    if num >= length:
        for i in range(length, num+1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])
    print('{} {}'.format(zero[num], one[num]))


if __name__ == "__main__":
    T = int(input())

    for i in range(T):
        N = int(input())
        zero = [1, 0, 1]
        one = [0, 1, 1]

        fibonacci(N)
