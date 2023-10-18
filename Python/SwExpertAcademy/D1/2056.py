# 2056 _ 연월일 달력
# 연월일 순 8자리 날짜가 입력됨

# first 유효한지 아닌지 판단 (유효X -> -1 출력)
### 월값은 1~12값 가지기
### 일값 -> 각 월 마다 예외처리???(조건문 해가지고)
### 31: 1,3,5,7,8,10,12
### 30: 4,6,9,11
### 28: 2

# 유효한 값은 2024/10/11 처럼 슬러쉬로 년월일 구분되게 해서 출력 해주기

T = int(input())

# 월에 대한 인덱스 4,5
## 4 : 0 or 1 이어야되
### 4가 0인경우 0 이면 안되 나머지는 가능
### 4가 1인경우 5는 0 1 2 여야 되
# 일에 대한 인덱스 6,7

for i in range(T):
    temp_value = str(input())
    il_value = temp_value[6] + temp_value[7]
    # print(il_value)
    # print(temp_value[4])
    if int(temp_value[4]) != 0 and int(temp_value[4]) != 1:
        print(f'#{i+1} -1')
    elif int(temp_value[4]) ==1:
        if int(temp_value[5]) != 0 and int(temp_value[5]) != 1 and int(temp_value[5]) != 2:
            print(f'#{i+1} -1')
        elif int(temp_value[5]) == 0 or int(temp_value[5]) == 2: # 10, 12 31일까지
            if int(il_value) > 31:
                print(f'#{i+1} -1')
            else:
                result = temp_value[0:4] + '/' + temp_value[4:6] + '/' + temp_value[6:]
                print(f'#{i+1} {result}')
        elif int(temp_value[5]) == 1:
            if int(il_value) > 30:
                print(f'#{i+1} -1')
            else:
                result = temp_value[0:4] + '/' + temp_value[4:6] + '/' + temp_value[6:]
                print(f'#{i+1} {result}')
    # 10, 11, 12 끝
    elif int(temp_value[4]) ==0:
        if int(temp_value[5]) == 2: # 2월인경우 28까지
            # print('2월')
            if int(il_value) > 28:
                print(f'#{i+1} -1')
            else:
                result = temp_value[0:4] + '/' + temp_value[4:6] + '/' + temp_value[6:]
                print(f'#{i+1} {result}')
        elif int(temp_value[5]) == 4 or int(temp_value[5]) ==6 or int(temp_value[5]) ==9 :# 4,6,9 인경우 30까지
            if int(il_value) > 30:
                print(f'#{i+1} -1')
            else:
                result = temp_value[0:4] + '/' + temp_value[4:6] + '/' + temp_value[6:]
                print(f'#{i+1} {result}')
        elif int(temp_value[5]) ==0:
            print(f'#{i+1} -1')
        else: # 31일 까지
            if int(il_value) > 31:
                print(f'#{i+1} -1')
            else:
                result = temp_value[0:4] + '/' + temp_value[4:6] + '/' + temp_value[6:]
                print(f'#{i+1} {result}')
    else: # 0 인경우
        print(f'#{i+1} -1')


#### 풀이법 2 딕셔너리 활용 __ 풀이 아름답네
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
for test_case in range(1, T + 1):
    case = str(input())
    year = case[0:4]
    month = case[4:6]
    day = case[6:8]

    answer = ''
    if 0 < int(month) < 13 and 0 < int(day) <= days[int(month)]:
        answer = year + '/' + month + '/' + day
    else:
        answer += '-1'

    print("#" + str(test_case) + " " + answer)


#### 풀이법 3
t = int(input())
month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(1, t + 1) :
    data = input()
    result = [data[:4]]

    if int(data[4:6]) in month :
        result.append(data[4:6])
    else :
        print('#%d %d' % (i, -1))
        continue

    if 1 <= int(data[6:]) <= day[int(data[4:6])-1] :
        result.append(data[6:])
    else :
        print('#%d %d' % (i, -1))
        continue

    print('#%d %s' % (i, "/".join(result)))