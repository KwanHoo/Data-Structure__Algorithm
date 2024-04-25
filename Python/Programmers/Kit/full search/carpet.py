# 알고리즘 고득점 KIT _ 완전탐색
# 카펫

def solution(brown, yellow):
    # 전체 개수
    grid = brown + yellow;

    for n in range(3, int(grid ** 0.5) +1):
        if grid % n !=0: continue

        m = grid // n

        if (n-2) * (m-2) == yellow:
            return [m, n]


def solution2(brown, yellow):
    answer = []
    yellow_x = 0
    yellow_y = 0
    for i in range(1, yellow+1):
        if yellow % i == 0:
            yellow_x = yellow // i
            yellow_y = i
            if 2*yellow_x + 2*yellow_y + 4 == brown:
                answer.append(yellow_x+2)
                answer.append(yellow_y+2)
                break
            answer.sort(reverse = True)
    return answer