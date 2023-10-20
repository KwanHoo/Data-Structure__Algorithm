# 1938 아주 간단한 계산기

# 두 개 자연수 사칙연산

F, S = map(int, input().split())

sum_rst = 0
mul_rst = 0
min_rst = 0
div_rst = 0

# 더하기
sum_rst = F + S

# 빼기
min_rst = F - S

# 곱하기
mul_rst = F * S

# 나누기(몫)
div_rst = F // S

print(sum_rst)
print(min_rst)
print(mul_rst)
print(div_rst)
