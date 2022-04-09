## 백준
## 10870번 : 피보나치수 5
## 수학, 구현, 재귀


# 0, 1 시작
# 0, 1, 1, 2, 3, 5, 8, ...
# Fn = Fn-1 + Fn-2

def Pibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return  1
    else:
        return Pibo(n-1) + Pibo(n-2)



if __name__ == "__main__":
    N = int(input())
    out = Pibo(N)
    print(out)