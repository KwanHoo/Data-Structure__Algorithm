# 문제집) Python 배우기 (1~50)
## 10988_팰린드롬인지 확인하기
# 브론즈 2

words = list(str(input()))

## solve1) re 슬라이싱 역으로 이용
re = words[::-1]
result = 1

# for i in range(len(re)):
#     if words[i] == re[i]:
#         pass
#     else:
#         result = 0
#         break
# print(result)


## solve2) 인덱스로 같은지 조회 가능
for i in range(len(re)):
    temp = len(re) -i -1
    # print(i,temp)

    if words[i] == words[temp]:
        pass
    else:
        result = 0
        break
print(result)
