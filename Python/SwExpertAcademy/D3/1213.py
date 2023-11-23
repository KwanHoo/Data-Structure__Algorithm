# 1213_String


T = 10
for _ in range(T):
    tcc = int(input())
    pan = input()
    mj = input()

    plen = len(pan)
    cV = 0
    for i in range(len(mj)-plen):
        if pan == mj[i:i+plen]:
            cV += 1

    # 마지막 10번째 케이스
    if  mj[-plen:] == pan:
        cV +=1
    print(f'#{tcc} {cV}')


