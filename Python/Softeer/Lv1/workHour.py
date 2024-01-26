# 근무 시간
# Lv.1

# 총 근로 시간이 법정근로시간을 초과하지 않아야함
#! 식사 시간 등 근무 외 시간을 근무 시간에서 제외하지 않음

hour = 0
minute = 0
for _ in range(5):
    S, E = map(str, input().split())

    sh = int(S[0:2])
    sm = int(S[3:])

    eh = int(E[0:2])
    em = int(E[3:])

    # print(sh, sm, eh, em)
    if em-sm <0:
        hour +=eh-sh-1
        minute += 60+em-sm
    else:
        hour += eh-sh
        minute += em-sm

# print(hour, minute)
result = hour * 60 + minute

print(result)