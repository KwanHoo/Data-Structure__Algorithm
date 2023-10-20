# 1933 간단한 N의 약수

# 입력 N 정수
# 정수 N의 약수를 오름차순으로 출력하는 프로그램 작성

## 약수 출력이라

N = int(input())
rst_list = ''
# 나누엇을때 나머지가 0이면 약수임

for i in range(1, N+1):
    if N % i == 0: # 나머지 0 : i 는 약수임
        rst_list += str(i)
        rst_list += ' '

print(rst_list)
