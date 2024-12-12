# 가장 가까운 같은 글자

##  딕셔너리 활용
def solution(s):

  answer = []
  di = {}

  for i in range(len(s)):
    ## 딕셔너리에 없는 경우 : 처음 : -1
    if s[i] not in di:
      answer.append(-1)
    else: ## 있는 경우 : 몇번째 앞인지 계산
      answer.append(i-di[s[i]])
    di[s[i]] = i ## 딕셔너리 내 초기화
    print(i,di, answer)

  return answer