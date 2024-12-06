# 프로그래머스 LV1 자릿수 더하기

def solution(n):
    answer = 0
    print(n)
    # 입력값 스트링 변환
    temp = str(n)

    # 반복문 내에서 누적섬
    for i in range(len(temp)):
        answer += int(temp[i])
    return answer