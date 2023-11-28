# 14692_통나무 자르기

T = int(input())

for tc in range(T):
    L = int(input())

    if L%2 == 0:
        result = 'Alice'
    else:
        result = 'Bob'

    print(f'#{tc+1} {result}')