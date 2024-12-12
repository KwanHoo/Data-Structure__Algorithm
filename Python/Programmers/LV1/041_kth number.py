# k번째 수

def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        ## 명령 세팅
        start = commands[i][0]
        end = commands[i][1]
        k = commands[i][2]

        ## 배열 슬라이싱
        temp = array[start - 1:end]
        temp.sort() ## 정렬

        result = temp[k - 1] ## k번재 수 추출
        answer.append(result)
    print(answer)

    return answer