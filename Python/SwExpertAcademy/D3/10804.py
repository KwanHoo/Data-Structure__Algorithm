# 10804_문자열의 거울상

T = int(input())

for tc in range(T):
    first = list(map(str, input()))

    words = []

    for  item in first[::-1]:
        words.append(item)

    mirror = ''
    for i in range(len(words)):
        if words[i] == 'b':
            mirror += 'd'
        elif words[i] == 'd':
            mirror += 'b'
        elif words[i] == 'p':
            mirror += 'q'
        elif words[i] == 'q':
            mirror += 'p'

    print(f'#{tc+1} {mirror}')

