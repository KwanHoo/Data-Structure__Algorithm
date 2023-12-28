# 03_문자열 뒤집기

# 뒤집는 것은 1을 0으로, 0을 1로 바꾸는 것을 의미함
## 다솜이는 문자열 S에 있는 모든 숫자를 전부 같게 만들려고함
## 다솜이가 해야하는 행동의 최소 횟수
## 행동은 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것임



## 최소 판별을 어떻게 하지??
## -> 아이디어
### 문자 묶음 블럭 만큼 뒤집어야함.
# 000 11 00 1의 블럭
# 111 00 11
##!! 전부 0으로 바꾸는 경우와 전부 1로 바꾸는 경우 중에서 더 적은 횟수를 가지는 경우를 계산

# S = str(input())

# count0 = 0  # 전부 0으로 바꾸는 경우
# count1 = 0  # 전부 1로 바꾸는 경우
#
# # 0 판별
# if S[0] == 1:
#     count0 += 1
# for i in range(1,len(S)):
#     if S[i] == '0':
#         pass
#     elif S[i] == '1' and S[i-1] == '0':
#         count0 += 1
#     else:
#         pass
#         # 1,1 0,1)
#
# # all 1 판별
# if S[1] == 0:
#     count1 += 1
# for j in range(1, len(S)):
#     if S[j] == '0' and S[j-1] == '1':
#         count1 += 1
#     else:
#         pass
#
# result = min(count0, count1)
#
# print(count0, count1, result)

# 23.12.28 solve : 13
#--> 풀이 잘못 된거 같음

# 해답
data = input()
count0 = 0  # 전부 0으로 바꾸는 경우
count1 = 0  # 전부 1로 바꾸는 경우

# 첫 번째 원소에 대해서 처리
if data[0] == '1':
    count0 += 1
else:
    count1 += 1

# 두 번째 원소부터 모든 원소를 확인하며
for i in range(len(data) -1):
    if data[i] != data[i+1]:
        # 다음 수에서 1로 바뀌는 경우
        if data[i + 1] == '1':
            count0 +=1
        # 다음 수에서 0으로 바뀌는 경우
        else:
            count1 +=1
result = min(count0, count1)
print(result)