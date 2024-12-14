# 영어 끝말잇기


def solution(n, words):
    for i in range(1, len(words)):
        # 첫글자 != 앞단어 뒷글자 또는 현단어가 뒤에 단어들 중 있는경우:
        ## 중복 단어가 나온거임!!,
        if words[i][0] != words[i - 1][-1] or words[i] in words[:i]:
            print('if', i, n)

            return [(i % n) + 1, (i // n) + 1]
    else:
        return [0, 0]
