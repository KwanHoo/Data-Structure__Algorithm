## 백준_2012번
## 등수 매기기
## 실버3
# 그리드문제

N = int(input())
nlist = []                          # 학생들 예상등수 리스트
tlist = [i for i in range(1,N+1)]   # 정상 등수 리스트
sumadd = 0

# 학생들 예상 등수 입력 받는 부분
for i in range(N):
    temp = int(input())
    nlist.append(temp)

nlist.sort()            # 오름차순 정렬

# 불만도 구하는 부분
for j in range(N):
    n1 = nlist[j]
    t1 = tlist[j]

    sumadd += abs(t1-n1)

## 총합 최소의 불만도
print(sumadd)
