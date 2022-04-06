##* 스택 : 후입선출 LIFO
##* 파이썬은 스택을 이용할때 별도의 라이브러리 사용 필요 없음
##* 기본 리스트에 append()와 pop() 이용

stack = []

stack.append(5)
stack.append(2)
stack.append(200)
stack.append(400)
stack.pop()
stack.append(300)
stack.append(25)
stack.pop()

##* 최하단 원소부터 출력
print(stack)

##* 최상단 원소부터 출력
print(stack[::-1])

