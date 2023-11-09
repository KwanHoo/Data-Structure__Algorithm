# 1288_새로운 불면증 치료법

# 입력 받은 N의 배수로 커짐
# 0~9까지 모두 숫자 나오면 카운팅 멈춤

T = int(input())

for tc in range(T):
    pan = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    vigo = []
    N = int(input())
    first = N           # 배수 시킬 첫번째 값 변수
    tal = True          # while문 탈출
    count = 1           # K값임

    while tal:
        temp = str(N)

        for i in range(len(temp)):
            if temp[i] not in vigo:     # 자리수 기여부 판별
                vigo.append(temp[i])


        if len(vigo) == len(pan):   # 루프 탈출 flag
            tal = False
        else:
            count += 1
            N = first * count

    print(f'#{tc+1} {temp}')