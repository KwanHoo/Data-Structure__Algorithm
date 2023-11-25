# 11445_무한 사전

## P와 Q 사이에 다른단어가 없다 : P다음 단어가 Q라는 거임

T = int(input())

for tc in range(T):
    P = input().rstrip() # 공백제거 해주어야함
    Q = input().rstrip()

    if P + 'a' == Q:
        print(f'#{tc+1} N')
    else:
        print(f'#{tc+1} Y')