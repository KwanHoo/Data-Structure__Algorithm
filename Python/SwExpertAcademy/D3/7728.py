# 7728_다양성 측정


T = int(input())

for tc in range(T):
    panN = str(input())
    numL = ['1','2','3','4','5','6','7','8','9','0']
    result = 0
    for i in range(len(panN)):
        temp = panN[i:i+1]

        if temp in numL:
            result += 1
            numL.remove(temp)

    print(f'#{tc+1} {result}')

# 파이썬 제출 X