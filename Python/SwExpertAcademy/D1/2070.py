# 2070 _ 큰 놈, 작은 놈, 같은 놈
# 2개의 수를 입력 받아 크기 비교하여 등호 또는 부등호 출력

# input
# 1) T:테스트케이스 수
# 2) 테스트 케이스 입력,,,,

# output
# #1 <
# #2 = ..

T = int(input())    # 테스트케이스 수 입력 받는 부분

temp_result = []    # 부등호 결과값 저장 리스트 부붑ㄴ
for i in range(T):  # 루프문 테스트 케이스 수만큼 반복
    input_list = list(map(int, input().split()))    # 입력 받는 부분 줄로 수만큼
    first_v = input_list[0]
    second_v = input_list[1]
    result_v = ''           # 결과부등호 값 저장되는 변수
    if first_v > second_v:  # 두개 입력값 비교하는 조건문 부분
        result_v = '>'
    elif first_v < second_v:
        result_v = '<'
    else:
        result_v = '='
    temp_result.append(result_v)    # 비교되어서 도출된 변수값 리스트에 저장함

##* 하단은 output 양식에 맞게 포맷스트링 이용해서 출력되게 작업되는 부분
num_v = 1
for i in temp_result:
    print(f'#{num_v} {i}')  # 포맷스트링 이용하여 숫자값이랑 리스트 부등값 출력되게
    num_v += 1              # 숫자값 증가되는 부분

