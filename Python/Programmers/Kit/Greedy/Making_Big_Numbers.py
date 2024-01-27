# 알고리즘 고득점 KIT _ 탐욕법
# 큰 수 만들기

#만들어질수 있는 모든 숫자의 조합 : combinations 함수 이용
## 스택으로 일단 들어오는 형식임
## 지금 들어온 스택값이 기존 point 값 보다 크면 기존 마지막 값 제거 (단, k수 만큼)

N, K = input().split()
N = str(N)
K = int(K)

# 참고 풀이
def solution(number, k):
    # 스택 선언
    stack = []

    # number의 길이만큼 for loop
    for num in number:
        # 1. 제거할 수 k가 남았고
        # 2. 스택에 값이 있고
        # 3. 스택의 마지막 값이 num보다 작다면
        # 제거 후 제거할 수 k를 1씩 감소
        while k > 0 and stack and stack[-1] < num:
            stack.pop()
            k -= 1
        # 스택에 num 추가
        stack.append(num)

    # k가 남아있는 경우 - 테스트 케이스 number: "93939", k: 2, 출력: 999, 실제정답: 99
    if k != 0:
        stack = stack[:-k]

    # 배열을 문자열로 바꿔주고 반환
    result = ''.join(stack)
    print(result)
    return result

solution(N,K)


# def solution(number, k):
#     answer = ''
#     numlist = []
#     for i in range(len(number)):
#         w = int(number[i])
#         numlist.append(w)
#
#     # print(numlist)
#     numlist.sort()      # 오름차순 정렬됨
#     # print(numlist)
#
#     for j in range(k):
#         x =numlist[j]
#         numlist.remove(x)
#
#     print(numlist)
#     numlist.sort(reverse=True)
#     print(numlist)
#     return answer