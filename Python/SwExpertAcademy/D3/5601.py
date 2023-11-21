# 5601_쥬스 나누기

# N명의 사람이 1리터의 쥬스를 나누어 각자 잔에 따라 마심
# 모든 사람이 목마른 상태이기 떄문에 최대한 쥬스를 마시고자 최선의 전략을 쓴다고 가정
# -> 모두 공평하게 1/N 만큼 먹음

T = int(input())


for tc in range(T):
    N = int(input())
    temp = ''
    for i in range(1,N+1):
        temp2 = '1' + '/' + str(N)
        temp = temp + temp2 + ' '
    # print(temp)
    print(f'#{tc+1} {temp}')

# 파이썬 제출 X