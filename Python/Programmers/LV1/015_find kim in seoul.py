# 서울에서 김서방 찾기

def solution(seoul):
    answer = ''
    temp = seoul.index("Kim")
    answer = "김서방은 " + str(temp) + "에 있다"
    return answer