## 백준
## 10872번 : 팩토리얼
## 수학, 구현, 재귀

## N! 출력


# 2! = 2 * 1
# 3! = 3 * 2!
# 4! = 4 * 3!

def factorial(n):
    if n == 1:
        return 1
    elif n == 0:
        return 1
    else:
        result = n * factorial(n-1)

    return result

if __name__ == '__main__':
    N = int(input())
    output = factorial(N)
    print(output)
