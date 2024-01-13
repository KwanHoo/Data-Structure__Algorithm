## 백준_1543번
## 문서 검색
## 실버5
# 그리드문제

## 중복되어 세는 것은 빼고 세야함
## 최대 몇번 등장하는가?

M = str(input())
S = str(input())

count = 0

ml = len(M)
sl = len(S)
i = 0
while i != ml:
    temp = M[i:i+sl]
    if temp == S:
        count += 1
        i += sl
    else:
        i += 1

print(count)