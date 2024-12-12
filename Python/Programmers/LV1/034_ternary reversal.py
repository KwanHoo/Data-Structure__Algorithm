# 3진법 뒤집기

def solution(n):
    answer = 0
    result = ''

    # 10 -> 3진법
    while n > 0:
        result = str(n % 3) + result  # 나머지로 3진법 표현
        n = n // 3

    print(result)

    # 3 -> 10진법
    for i in range(len(result)):
        answer += int(result[i]) * 3 ** i

    return answer