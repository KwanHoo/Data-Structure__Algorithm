# 1859_백만 장자 프로젝트

# 미래를 보는 능력 으로 사재기 할려고 하는..
# 조건
# 1. 원재는 연속된 N일 동안의 물건의 매매가를 예측하여 알고 있음
# 2. 당국의 감시망에 걸리지 않기 위해 하루에 최대 1만큼 구입할 수 있음
# 3. 판매는 얼마든지 할 수 있음

# ex) 3일 동안의 매매가가 1, 2, 3 이라면 처음 두날에 원료를 구매하여 마지막 날에 팔면 3의 이익을 얻을 수 있음

## input
# T : 테스트 케이스의 수
# N1 : 테스트 케이스 별 입력되는 데이터 수
# N2 : 각 날의 매매가  N1개 입력됨

## output
# 각 날에 얻게 되는 이익

# sol)
## -하루에 구매 1개 할 수도 안할수도 있는 흠
## 아무것도 사지 않는것이 이득인 케이스도 있음 !! (흠)
# 뒤에 있는 인덱스의 데이터가 앞의 데이터보다 큰 경우 차이가 양의 정수가 나옴 -> 이게 이익을 얻는 부분임
# 인덱스를 하면서 앞의 숫자 중 작은 수가 있는지 확인??
## 뒤에 있는 값이 큰 날이 있으면 무조건 구입을 하고 판매를 진행해야 함

## 흠 파는 시점은 최대 값이 있는 시점으로 판매를 진행해야 함

# T = int(input())
# NUM = 1
# for x in range(T): # 입력 받은 T 만큼 반복
#
#     N1 = 0
#     N1 = int(input())
#     N2 = ''
#     profit = 0
    #temp = list(map(str, input().split())) # 리스트 안해주면 map 객채로 출력이 되게 되네 ㅎㄷ
    #for j in range(N1):
    #     N2 = N2 + temp[j] + ' '
    #     N2 = N2 + temp + ' '
    # print(N2)
    # print(temp)
    # print(N2)
    ## N2에 스트링 입력 데이터 넣어둠

    ## 내가 봤을때 데이터 어차피 비교를 해야되서 데이터를 스트링으로 해둘 필요는 없음
    ## 내가 안에서 작업할 때 스트링 말고 그냥 int로 비교하기만 하면 되기에 맞죵 ㅎㅎㅎ

    # temp = list(map(int, input().split()))
    # print(max(temp)) # 리스트 내 최대값 찾기 max(변수)
    # print(temp.index(max(temp))) # 리스트 내 인덱스 찾기
    # max_list_value = max(temp)
    # max_list_value_index = temp.index(max_list_value)
    # if max_list_value_index == 0: # 첫번째 인덱스가 max 인 경우
    #     print(f'#{NUM} {profit}')
    #     NUM += 1
    # else:
    #
    #     print(f'#{NUM} {profit}')
    #     NUM += 1

### solve_idea : 배열을 거꿀로 순회!!
N = int(input()) # 전체 TC 갯수
for i in range(N): # TC마다
    M = int(input()) #배열의 길이 (안쓰임)
    answer = 0 #출력할 정답
    arr = list(map(int, input().split())) #배열 입력 받기
    sellPrice = 0 #현재 판매가격(최댓값)

    for val in arr[::-1]: # 배열 거꾸로 순회
        if val >= sellPrice: #현재 값이 최댓값보다 크거나 같다면
            sellPrice = val #최댓값 업데이트
        else:
            answer += sellPrice - val #아니라면 정답값에 가격차이를 더한다. (현재 값에 구매해서 최댓값에 판다)
    print("#", i + 1, " ", answer, sep="") #출력 양식에 맞춰서 출력
