# 백준
# 타입 : 동적 프로그래밍, 그리디 알고리즘
# 2839번 : 설탕배달


# remainder
# 나머지 연산자 : %
# quotient
# 몫 연산자 : //

def test1():
    sugar_total = int(input())  # 총 설탕 무게

    rem_five = sugar_total % 5  # 5로 나눈 나머지
    rem_five_three = rem_five % 3  # 5 -> 3로 나눈 나머지
    rem_three = sugar_total % 3
    rem_three_five = rem_three % 5
    total = 0
    # 5로 나누었을때 나머지 경우의 수 [0, 1, 2, 3, 4]
    # 가능 => 나머지 0인 경우
    if rem_five == 0:
        total += sugar_total//5
        print(total)

    # 5 -> 3 가능
    # 나머지 [1, 2, 3, 4] 중
    # 3으로 나누었을때 0인 경우 위의 나머지 3인 경우
    elif rem_five_three == 0:
        total = total + sugar_total//5 + rem_five//3 
        print(total)
        
    # 5,3 둘다 불가능
    # 3으로 딱 가능
    # 3=> 5로 가능
    else:
        if rem_three == 0:
            total += sugar_total//3
            print(total)
        # 나머지 [1, 2, 4]
        # 3 -> 5 가능
        elif rem_three_five == 0:
            total = total + sugar_total//3 + rem_three//5
            print(total)
        else:    
            print(-1)

# 코드 문제 있음 
# 입출력 케이스 5
# 입력 11의 경우 5 + 6으로 2개의봉지가 정답
# test1 함수의 코드로는 11을 5로 나누어 나머지 1, 3으로 나머지 2의 값을 얻게됨 (출럭 : -1)
# test1()




def test2():
    sugar_total = int(input())  # 총 설탕 무게

    quot_five = sugar_total // 5
    quot_three = sugar_total // 3
    total = 0
    # range(start, stop, step)
    # for i in range(quot_five, -1, -1): # 리버스
    for i in range(quot_five+1):
        if (i == (quot_five)):
            print(-1)
            break
        else:
            # minus_quot = sugar_total - quot_five * 5
            sugar_total -= i * 5
            rem_five = sugar_total % 5  # 5로 나눈 나머지
            rem_five_three = rem_five % 3  # 5 -> 3로 나눈 나머지
            rem_three = sugar_total % 3
            rem_three_five = rem_three % 5

            if rem_five == 0:
                total += sugar_total//5 + i
                print(total)
                break

            # 5 -> 3 가능
            # 나머지 [1, 2, 3, 4] 중
            # 3으로 나누었을때 0인 경우 위의 나머지 3인 경우
            elif rem_five_three == 0:
                total = total + sugar_total//5 + rem_five//3 + i
                print(total)
                break

            # 5,3 둘다 불가능
            # 3으로 딱 가능
            # 3=> 5로 가능
            else:
                if rem_three == 0:
                    total += sugar_total//3 + i
                    print(total)
                    break
                # 나머지 [1, 2, 4]
                # 3 -> 5 가능
                elif rem_three_five == 0:
                    total = total + sugar_total//3 + rem_three//5 + i
                    print(total)
                    break
# 반례 32 => 답 : 8(5*4 + 3*4) but. output?10
# test2()


def test3():
    sugar_total = int(input())  # 총 설탕 무게
    quot_five = sugar_total // 5  
    quot_three = sugar_total // 3 

    value_t = 0
    value_f = 0
    breakValue = True

    for i in range(quot_three+1):
        for j in range(quot_five+1):
            if ((i*3)+(j*5) == sugar_total):
                value_t = i
                value_f = j
                breakValue = False
                break
        if(breakValue == False):
            break

    if value_t*3 + value_f*5 == sugar_total:
        print(value_t+value_f)
    else:
        print(-1)
# 11 => 3
# 32 => 8
# 제출 코드 성공!

test3()
