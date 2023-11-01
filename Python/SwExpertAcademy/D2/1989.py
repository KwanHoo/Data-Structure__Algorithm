# 1989_초심자의 회문 검사

# 회문(palindrome) : 거꾸로 읽어도 제대로 읽은 것과 같은 문장이나 낱말
# 회문이면 1, 아니면 0 (바밤바)

#! 길이 : 3이상 10이하

T = int(input())

# 테스트케이스 1개 오답으로 나옴.. (9/10)
for i in range(T):
    check_s = str(input())
    s_len = len(check_s)
    s_len_d = s_len % 2 # 길이, 짝수 0  홀수 1
    s_len_m = s_len // 2
    result = 1
    # ifbreak = False

    if s_len_d == 0:
        for j in range(0, s_len_m):
            if check_s[j] != check_s[-j-1]:
                result = 0
                break
    else:
        for k in range(0, s_len_m-1):
            if check_s[k] != check_s[-k-1]:
                result = 0
                break

    print(f'#{i+1} {result}')

## solve: 리스트 역순 이용
for i in range(1, T + 1):
    answer = 0
    a = list(input())
    r = a[::-1] # 리스트 역순 저장

    if a == r:
        answer = 1
    else:
        answer = 0
    print("#%d" % i, answer)