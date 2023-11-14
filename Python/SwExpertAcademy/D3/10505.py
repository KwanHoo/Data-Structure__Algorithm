# 10505_소득 불균형

T = int(input())

for tc in range(T):
    N = int(input())

    nlist = list(map(int, input().split()))

    numP = 0
    suml = sum(nlist)
    avgl = suml / N

    sortl = sorted(nlist)

    for i in range(len(sortl)):
        if sortl[i] <= avgl:
            numP += 1
        else:
            break

    print(f'#{tc+1} {numP}')