# 이진 변환 반복하기

## 길이 -> 이진법 작업 추가 필요
# 1) 0 제거
# 2) x의 길이 2진법 변환
## 반복 => 1이 될 때 까지
##* return : [이진변환횟수, 0 제거 갯수]

def solution(s):
    answer = []
    count = 0
    zeroc = 0

    # zeroc = s.count("0")

    while s != '1':
        print(count, s, zeroc, count)

        c = s.count("1")  ## 2진수에서 1의 개수
        z = s.count("0")  ## 2진수에서 0의 개수
        temp = c * "1"  ## temp -> ex) 1111

        sl = len(temp)

        ttt = bin(sl)  # 10진수 2진수 변환
        s = ttt

        zeroc += z  ##* 0의 개수
        count += 1  ##* 변환햇수 증가
        if int(s, 2) == 1:
            ##* int('x', radix) : radix 진수로 표현
            ##* int('x',2) -> 2진수로 표현되는 거임
            ##* 조건문=> 1이 되어서 탈출!!
            break
        else:
            ##* 1아님! -> 2진수 0b로 시작 : 슬라이싱
            s = str(s[2:])
        # print(count, s, zeroc)

    answer = [count, zeroc]

    return answer