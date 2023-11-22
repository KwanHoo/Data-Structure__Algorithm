# 5431_민석이의 과제 체크하기

# 수강생 N명

## 과제를 제출하지 않은 사람의 번호를 오름차순으로 출력하는 프로그램 작성

T = int(input())

for tc in range(T):
    N, K = map(int, input().split())
    je = list(map(int, input().split()))
    nje = ''

    for i in range(1,N+1):
        if i not in je:
            nje = nje + str(i) + ' '

    print(f'#{tc+1} {nje}')