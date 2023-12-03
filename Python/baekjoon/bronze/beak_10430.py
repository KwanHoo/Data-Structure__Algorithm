# 문제집) Python 배우기 (1~50)
## 10430_나머지
# 브론즈 5

A, B, C = map(int, input().split())

result1 = (A+B) % C
result2 = ((A%C) + (B%C)) % C
result3 = (A*B) % C
result4 = ((A%C) * (B%C)) % C

print(result1)
print(result2)
print(result3)
print(result4)