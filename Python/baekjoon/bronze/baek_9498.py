## 백준 9498
## 시험성적
## 조건문, 구현

def examScore(n):
    pass
    if n <101 and n > 89:
        print('A')
    elif n > 79:
        print('B')
    elif n > 69:
        print('C')
    elif n > 59:
        print('D')
    else:
        print('F')

if __name__ == "__main__":
    N = int(input())
    examScore(N)


''' 참고 숏코드
print("FFFFFFDCBAA"[int(input())//10]) 
0~5 : F
6: D
7: C
8: B
9: A
10: A
"문자열"[인덱스]
//연산자 :  나누고 정수만 남김
'''