# 2027 대각선 출력하기

# 주어진 텍스트 그대로 출력

# print 문 걍 이용
print('#++++')
print('+#+++')
print('++#++')
print('+++#+')
print('++++#')

## 하지만 이게 1억개라고 생각하면 위 방식으로 풀이 할 수 없음
N = int(input()) #입력값이라고 가정
# N = 5
for i in range(N):
    temp_str = ''

    for j in range(N):
        if i == j:
            temp_str += '#'
        else:
            temp_str += '+'
    print(temp_str)
