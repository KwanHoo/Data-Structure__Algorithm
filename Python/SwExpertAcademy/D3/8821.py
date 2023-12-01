# 8821_적고 지우기

T = int(input())

# 없는 상태에서 적고 또 나오면 지우고 반복

for tc in range(T):
    numl = input()
    box = []

    for i in range(len(numl)):
        val = numl[i]

        if val not in box:
            box.append(val)
        else:
            box.remove(val)

        # print(box, i)
    lb = len(box)
    print(f'#{tc+1} {lb}')

# 파이썬 제출 불가