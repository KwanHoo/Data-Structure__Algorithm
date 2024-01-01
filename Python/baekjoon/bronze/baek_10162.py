# 문제집) Python 배우기 (1~50)
## 10162_전자레인지
# 브론즈 3

## A,B,C = 5m, 1m, 10s
#버튼은 최소로조작

### 접근1) 몫으로 : fail
# A, B, C = 300, 60, 10
# count1, count2, count3 = 0,0,0
# rest1, rest2, rest3 = 0,0,0
#
# T = int(input())
# if T // A != 0:
#     count1 = T // A
#     rest1 = T % A
#
#     if rest1 // B != 0:
#         count2 = rest1 // B
#         rest2 = rest1 % B
#
#         if rest2 // C != 0:
#             count3 = rest2 // C
#             print(count1, count2, count3)
#         else:
#             print(-1)
#     else:
#         if rest1 // C != 0:
#             count3 = rest1 // C
#             print(count1, count2, count3)
#         else:
#             print(-1)
#
#
# else:
#     if T // B != 0:
#         count2 = T // B
#         rest2 = T % B
#
#         if rest2 // C != 0:
#             count3 = rest2 // C
#             print(count1, count2, count3)
#         else:
#             print(-1)
#     else:
#         if T // C != 0:
#             count3 = T // C
#             print(count1, count2, count3)
#         else:
#             print(-1)



### 접근2) 나머지로_ greedy 문제
## else 부분인경우 어차피 0 이어서 생략가능
A, B, C = 300, 60, 10
count1, count2, count3 = 0,0,0
rest1, rest2, rest3 = 0,0,0

T = int(input())

if T % 10 != 0:
    # 1자리수 존재
    print(-1)
else:
    # A 몫 존재
    if (T // A) != 0:
        count1 += T//A
        T = T % A

    # B 몫 존재
    if (T // B) != 0:
        count2 += T//B
        T = T % B

    # C 몫 존재
    if (T // C) != 0:
        count3 += T//C

    print(count1, count2, count3)
