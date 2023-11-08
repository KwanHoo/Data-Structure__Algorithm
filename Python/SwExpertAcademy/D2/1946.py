# 1946_간단한 압축 풀기
# sol) 딕셔너리 활용

T = int(input())

for tc in range(T):
    N = int(input())
    iDic = {}
    for nc in range(N):
        ki, vi =  input().split()
        iDic[ki] = int(vi)
    # print(iDic)
    result = ''
    # 딕셔너리 키 값 리스트로 저장
    key_temp = []
    for key in iDic.keys():
        key_temp.append(key)

    # print(key_temp)
    e = 0 ## 갯수 토탈
    for k in key_temp:
        # print(iDic[k]) ## value
        temp = k * iDic[k]
        e += iDic[k]
        # print(temp)
        result += temp

    # print(result)
    print(f'#{tc+1}')
    s = 0
    for r in range(s, e, 10):
        # print(r) # 0, 10, 20
        # print(e-r)
        if e-r > 10:
            print(result[r:r+10])
        else:
            print(result[r:e])
