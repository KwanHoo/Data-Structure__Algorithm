## 백준 2480
## 주사위 세개
## 수학, 사칙연산, 조건문
import sys

def money(nums):
    a,b,c = nums.split()

    if a == b == c :
        result = 10000 + int(a) * 1000
    elif a == b or b == c:
        result = 1000 + int(b) * 100
    elif c == a :
        result = 1000 + int(c) * 100
    else:
        temp = max(a, b, c)
        result = int(temp) * 100

    return result

if __name__ == "__main__":
    N = sys.stdin.readline().strip()
    print(money(N))