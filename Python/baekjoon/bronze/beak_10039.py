# 문제집) Python 배우기 (1~50)
## 10039_평균 점수
# 브론즈 4



scoreL = []

# 5명 입력으로 주어짐
for _ in range(5):
    temp = int(input())

    # 40점 미만은 40점으로
    if temp < 40:
        temp = 40
    scoreL.append(temp)

result = int(sum(scoreL) / len(scoreL))

print(result)