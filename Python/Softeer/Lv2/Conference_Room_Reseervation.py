# 회의실 예약
# Lv.2

## 규칙
# - 9시 ~18시 이용가능
# - 회의실, 시작 시간, 종료 시각
# 종료시각 시단위로만 설정 가능
# 시간 서로 겹칠수 없음

# N : 회의실 갯수
# M : 회의 배정된 회의실 이름, 시작시각, 종려시각
N, M = map(int, input().split())
nl = []
Ml = []
num = [9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
for _ in range(N):
    temp = input()
    nl.append(temp)

for _ in range(M):
    r, s, t = map(str, input().split())
    Ml.append([r, s, t])

# 회의실 정렬
nl.sort()
Ml.sort()

rn = nl[0]
for i in range(M):
    nowrn, st, et = Ml[i][0], Ml[i][1], Ml[i][2]

    # 룸 변경 여부
    if rn == nowrn:
        if i+1 == M:
            # 마지막 룸인 경우
            # print('마지막 들어옴')
            # num에서 st~et 빼주기
            rn = nowrn
            for j in range(int(st),int(et)+1):
                # print('셋', rn, j, num)
                if j in num:
                    num.remove(j)
            ###! 마지막 결과 출력 !###
            print(f'Room {rn}:')
            if len(num) == 0:
                print("Not available")
                print("-----")
            else:
                # print('x avilable:')
                # print(rn, nowrn, num)
                count = 0  ## 예약가능수
                timel = []
                if num[0] == 9:
                    stp = 9
                    etp = 10
                    nowp = stp
                    for p in range(1, len(num)):
                        temp = num[p]
                        if nowp + 1 == temp:  # 연속된경우
                            ## 마지막 p 인경우
                            if p == len(num) - 1:
                                etp = temp
                                if etp == 18:
                                    word = str(stp) + '-' + str(etp)
                                else:
                                    word = str(stp) + '-' + str(etp + 1)
                                timel.append(word)
                                count += 1
                            else:
                                nowp = temp
                                etp = nowp
                        else:  # 비연속
                            if stp == 9:
                                stp = str('09')
                            if nowp == 9:
                                word = str(stp) + '-' + str(etp)
                            else:
                                word = str(stp) + '-' + str(etp + 1)
                            timel.append(word)
                            count += 1
                            stp = temp - 1
                            etp = stp + 1
                            nowp = temp
                print(f'{count} available:')
                for i in range(len(timel)):
                    print(timel[i])

                else:
                    stp = num[0]
                    etp = stp + 1
                    nowp = 0

        else:
            # num에서 st~et 빼주기
            rn = nowrn
            for j in range(int(st),int(et)+1):
                # print('첫', rn, j, num)
                if j in num:
                    num.remove(j)
    else: # 변경됨
        ###! 앞 룸 관련 출력해주기 !###
        print(f'Room {rn}:')
        if len(num) == 0:
            # a now = []
            print("Not available")
            print("-----")
        else:
            # print('x avilable:')
            # print(rn,nowrn, num)
            count = 0 ## 예약가능수
            timel = []
            if num[0] == 9:
                stp = 9
                etp = 10
                nowp = stp
                for p in range(1,len(num)):
                    temp = num[p]
                    if nowp+1 == temp:#연속된경우
                        ## 마지막 p 인경우
                        if p == len(num)-1:
                            etp = temp
                            if etp == 18:
                                word = str(stp) + '-' + str(etp)
                            else:
                                word = str(stp) + '-' + str(etp + 1)
                            timel.append(word)
                            count += 1
                        else:
                            nowp = temp
                            etp = nowp
                    else: #비연속
                        if stp == 9:
                            stp = str('09')
                        if nowp == 9:
                            word = str(stp) + '-' + str(etp)
                        else:
                            word = str(stp) + '-' + str(etp + 1)
                        timel.append(word)
                        count += 1
                        stp = temp-1
                        etp = stp+1
                        nowp = temp
            print(f'{count} available:')
            for i in range(len(timel)):
                print(timel[i])

            else:
                stp = num[0]
                etp = stp + 1
                nowp = 0
            print("-----")

        # num리스트 초기
        rn = nowrn
        num = [9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
        for j in range(int(st),int(et)+1):
            # print('둘', rn, j, num)
            if j in num:
                num.remove(j)






# 2024.01.26 _ 테스테키에스 1개 통과,