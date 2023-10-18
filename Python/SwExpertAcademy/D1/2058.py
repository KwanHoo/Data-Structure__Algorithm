# 2058 _ 자릿수 더하기
# 하나의 자연수를 입력 받아 각 자릿수의 합을 계산

# input
# 자연수 6789


# output
# 30

na_num = int(input())   # int 값으로 받은 자연수
str_nn = str(na_num)    # string 타입으로 바꿔줌

list_temp = []          # temp 리스트 선언
for i in range(0,len(str_nn)):  # range(0, 5) <- int는 iterable이 안되기에 range로 보완
    temp = str_nn[i]            # 스트링의 인덱스로 번호값 하나씩 temp리스트에 넣어줌
    list_temp.append(int(temp))

result_v = sum(list_temp)       # 리스트 sum() 으로 모두 더하기
print(result_v)