# 2043 서랍의 비밀번호

# 비밀번호 맞추기 , 1씩 증가함
# 시작 번호 : K
# 비밀번호 : P

P, K = map(int, input().split())

result = K - P
print(abs(result) + 1) # 절대값 함수 이용
