# 2007 패턴 마디의 길이

# 문자열에서 반복되는 패턴의 길이 출력

## 첫번째랑 같은 문자가 나오고
# T = int(input())
# count = 0
# first = ''
# second = ''
#
# for i in range(T):
#     string = str(input())
#     for j in range(len(string)):
#         # print(string[i])
#         string[j]
#         string[j+count]

# print(string)

## 슬라이싱 활용
T = int(input())
for test_case in range(1, T + 1):
    s = input()
    for j in range(1,10): # 마디의 최대 길이가 10
        if s[:j]==s[j:2*j]: # 슬라이싱 활용
            print(f'#{test_case} {j}')
            break

## 위의 코드로 최적화함
T = int(input())

for tc in range(1, T + 1):

    text = input()
    pattern = []
    next_pattern = []
    ans = 0
    for i in range(11):  # 마디의 최대 길이가 10이므로 range(11)
        pattern = text[:i]  # patten리스트에 패턴 입력
        next_pattern = text[i:i * 2]  # 다음 패턴 입력
        # print(pattern)
        # print(next_pattern)
        if i != 0 and pattern == next_pattern:  # 다음 패턴과 이번 패턴이 같은경우
            ans = len(pattern)  # 길이 출력
            break
    print('#{} {}'.format(tc, ans))