## 백준 2741
## N찍기
## [반복문], 구현

def nloop(n):
    for i in range(n):
        print(i+1)

if __name__ == "__main__":  
    N = int(input())
    nloop(N)


''' 참고 숏코드
print(*range(1,int(input())+1))
'''