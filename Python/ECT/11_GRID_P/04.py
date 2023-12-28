# 04 만들 수 없는 금액
import itertools

N = int(input())
nlist = list(map(int, input().split()))

sumMax = sum(nlist)

## 전체 금액값
dlist = [i+1 for i in range(sumMax)]
# print(dlist) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

sortl = sorted(nlist)

# print(sortl) [1, 1, 2, 3, 9]

setl = set(sortl)
# print(setl) {1, 2, 3, 9}
## 첫번째 필터 - 쌩 동전 값 다 날려
for i in setl:
    if i in dlist:
        dlist.remove(i)

# print(dlist) [4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16]

## 두번째 필터 - 더하는거 조합 //(순열은 중복되는거 있어서 조합으로)
sumPlist = []
for j in range(2, N+1):
    nPr = list(itertools.combinations(sortl, j))

    for k in range(len(nPr)):
        temp = sum(nPr[k])

        sumPlist.append(temp)

ssPl = set(sorted(sumPlist))

for m in ssPl:
    if m in dlist:
        dlist.remove(m)

## 결과 : 동전으로 만들 수 없는 양의 정수 금액 중 최솟값
print(dlist[0])