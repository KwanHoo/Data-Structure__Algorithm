## 백준
## 알람시계
## 조건문, 수학, 사칙연산

import sys

'''
45분 일찍 알람 성정하기

input H M (0 ≤ H ≤ 23, 0 ≤ M ≤ 59)

##! input 0 30  => 23 45
##* input 10 10 => 9 25
'''

def alram45(hour, minute):
    pass
    if hour != 0:
        if minute < 45:
            hour -= 1
            temp = 45 - minute
            minute = 60 - temp
        else:
            minute -= 45
    else:
        if minute < 45:
            hour = 23
            temp = 45 - minute
            minute = 60 - temp
        else:
            minute -= 45
    print(hour, minute)
    ##* return hour, minute
    ##! 런타임 에러 뜸
if __name__ == '__main__' :
    H, M = map(int, sys.stdin.readline().split())
    ##* setHour, setMinute = alram45(H, M)
    ##* print(setHour, setMinute)
    alram45(H,M)