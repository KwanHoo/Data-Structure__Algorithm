# 1983_조교의 성적 매기기

# 학기 끝나고, 학생들의 점수로 학점 계산

# 10개 평점 ( A+ A0 A- B+ B0 B- C+ C0 C- D0 )
## 중간(35%) + 기말(45%) + 과제(20%) = 총점

T = int(input()) #총테스트 케이스 수
for t in range(T):
    N, K = map(int,input().split())  ## 주의!! N 값으로 10~100사이 10배수값들어옴
    mid = 0     #중간
    fin = 0     #기말
    tesk = 0    #과제
    grade_temp = []
    grade = ['D0', 'C-', 'C0', 'C+', 'B-', 'B0', 'B+', 'A-', 'A0', 'A+']

    for i in range(N):
        mid, fin, tesk = map(int, input().split())
        temp_total = 0.35 * mid + 0.45 * fin + 0.2 * tesk
        grade_temp.append(temp_total)

    # print(grade_temp)
    find = grade_temp[K-1]
    # print(find)
    temp_sort = sorted(grade_temp)

    index_find = int(temp_sort.index(find) / (N//10)) ## 학생들에게 동일한 평점 부여 위해
    # print(index_find)
    result = grade[index_find]


    print(f'#{t+1} {result}')
