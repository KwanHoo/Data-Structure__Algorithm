# 금고털이
# Lv2

# 배낭은 W 까지 담을 수 있음
#in : 각 금속의 무게와 무게당 가격
#Out : 배낭을 채울 수 있는 가장 비싼 가격 출력

W, N = map(int, input().split())

mlist = []
for tc in range(N):
    M, P = map(int,input().split())
    mlist.append([P, M])

mlist.sort(key = lambda  x : -x[0])

result = 0
# print(mlist)
for j in range(N):
    # print(j, mlist[j][1], W)
    if mlist[j][1] < W:
        weight = mlist[j][1]
        price = mlist[j][0]
        temp = price * weight
        W -= weight
        result += temp
        # print("if",W, mlist[j][0], temp)

    else:
        temp = W * mlist[j][0]
        result += temp
        # print("el",W, mlist[j][0], temp)
        break

print(result)


# 접근1 : 무게 당 가격이 가장 큰 값 = P/M  => X

# 접근2 : P값 높은걸로 정렬 하고 각  M값 빼면서 W 값 0 될때까지 가격 더함
#
# W, N = map(int, input().split())
# mdic = {}
# # idic = {}
# result = 0
# # 입력받기
# for tc in range(N):
#     M, P = map(int, input().split())
#
#     mdic[M] = P
#     # idic[tc] = M
# #딕셔너리 value로 정렬
# smdic = sorted(mdic.items(), key=lambda x: x[1], reverse=True)
# # print(mdic)
# # print(idic)
# # print(smdic)
#
#
#
# for j in range(N):
#     weight, wprice = smdic[j][0], smdic[j][1]
#
#
#     if W > weight:
#         W -= weight
#         result += weight * wprice
#     else: # W < weight 그리고 W == weight 경우
#         result += W * wprice
#         break
#
#
# print(result)

## 접근 1
# W, N = map(int, input().split())
# mlist = {}
# pdic = {}
# olist = {}
#
# result = 0
# ## 갑 입력 받는 부분
# for tc in range(N):
#     M, P = map(int,input().split())
#
#     mlist[M] = P
#     olist[tc] = M
#     value = P/M
#     pdic[tc] = value
#
# ## 가장 비싼 가격 판별
# print(mlist)
# # print(pdic)
# print(olist)
#
# spdic = sorted(pdic.items(), key = lambda x: x[1], reverse=True)
# print(spdic)
#
# # test = spdic[0][0]
# # print(test)
# breakT = False
#
# while (W>0):
#     if breakT:
#         print("!!! breakT")
#         break
#     for j in range(N):
#         if W == 0:
#             break
#         index = spdic[j][0]     ## P/M이 가장 큰 인덱스
#         weight = olist[index]   ## mlist의 키값 조회 = 금속 무게
#         wprice = mlist[weight]  ## mlist의 해당 벨류 = 금속 무게당 가격
#
#         print("첫",index, weight, wprice)
#         mok = W // weight
#         na = W % weight
#         print("두", mok, na)
#         result += mok * weight * wprice
#         print("셋",result, W)
#         W = na
#
#         if j+1 ==N:
#             result += na *wprice
#             breakT = True
#
#
# print(result)


# slist = sorted(mlist)
# print(slist)