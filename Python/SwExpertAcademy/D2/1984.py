# 1984_중간 평균값 구하기

# 10개 수 입력받아, 최대수와 최소수를 제외한 나머지의 편균값을 출력
#! 소수점 첫째 자리에서 반올림한 정수를 출력
#! 0이상 10000이하의 정수

T = int(input())

for t in range(T):
    check_li = list(map(int, input().split()))
    # print(check_li)

    ## sort는 1, 11, 2 이렇게 정렬됨 -> 위에서 str로 인풋받아서 그런듯
    # li_sort = sorted(check_li)
    # print(li_sort)
    # filt_li = li_sort[1:-1]
    # print(filt_li)
    # sum_fir = sum(filt_li)
    # print(sum_fir)

    ## max, min 값 remove 하자
    max_li = max(check_li)
    check_li.remove(max_li)
    min_li = min(check_li)
    check_li.remove(min_li)

    sum = 0
    result = 0

    for i in range(len(check_li)):
        sum += check_li[i]

    result = round(sum/len(check_li))
    print(f'#{t+1} {result}')