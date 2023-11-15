# 11688_Calkin_Wilf tree 1

#! 루트 1/1
# 어떤 노드 a/b 의 왼쪽 자식은 a/a+b, 오른쪽 자식은 a+b/b

T = int(input())

for tc in range(T):
    mov = list(input())

    lenL = len(mov)
    a = 1
    b = 1
    A = 0
    B = 0
    for i in range(lenL):
        vali = mov[i]

        if i == 0:
            if vali == 'L':
                A = a
                B = a+b
            elif vali =='R':
                A = a+b
                B = b
        else:
            if vali == 'L':
                A = A
                B = A+B
            elif vali == 'R':
                A = A+B
                B = B

    print(f'#{tc+1} {A} {B}')
