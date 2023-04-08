## 구현_ 4-2 시각

# 전체 경우의 수 : 86400 가지

# H를 입력받기
H = int(input())

count = 0
for i in range(H + 1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)