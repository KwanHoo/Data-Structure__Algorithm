##* 큐 : 선입선출 FIFO
##! 데크(deque) 이용
##* 데이터 넣고 빼는 속도가 리스트 자료형에 비해 효율적
##* queue 라이브러리 보다 간단
from collections import deque

##* 큐 구현 위해 deque 라이브러리 사용
queue = deque()

queue.append(5)
queue.append(300)
queue.append(200)
queue.append(400)
queue.popleft()
queue.append(2000)
queue.append(32)
queue.popleft()

##* 먼저 들어온 순서대로 출력 FIFO
print(queue)
##* 다음 출력을 위해 역순
queue.reverse()
##* 나중에 들어온 원소부터 출력  
print(queue)

##* deque 객체로 출력되는데 리스트 자료형 변경시 list() 메서드 이용
##! list(queue)