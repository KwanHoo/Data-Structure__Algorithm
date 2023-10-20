# 2019 더블더블

# 1부터 주어진 횟수까지 2를 곱한 값(들) 출력
# 주의) 주어진 입력값은 30을 넘지 않음

# sol) 거듭제곱 연산자 이용
N = int(input())
rst_str = '1 '
first = 1
for i in range(1,N+1):
    temp = 2**i
    rst_str = rst_str + str(temp)
    rst_str += ' '

print(rst_str)