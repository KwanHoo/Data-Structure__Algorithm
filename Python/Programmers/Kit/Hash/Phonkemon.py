# 알고리즘 고득점 KIT _ 해시
# 폰켓몬

# 고를 수 있는 포켓몬 최대값 - 최대한 다양한 종류의 포켓몬 원함
# N마리중 N/2 마리 가능 -> 절반
## 같은 종류의 폰켓몬은 같은 번호를 가짐 : 종류에 따라 번호를 붙여 구분
# 다양한 포켓몬 원해 : 최대값
### return : 가장 많은 종류의 폰켓몬을 선택하는 방법을 찾아 그때의 폰켓몬 종류 번호의 개수를 return
#
### 풀이 ###
# 중복을 제거한 값을 구하기 위해 Set을 이용

nums = list(map(int, input().split()))

def solution(nums):
    answer = 0

    snum = set(nums)

    nl = len(nums)/2
    sl = len(snum)
    if sl < nl:
        answer = sl
    else:
        answer = nl
    return answer

solution(nums)

## 24.02.07 : 9m