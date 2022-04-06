# 백준
# 타입 : 그래프 이론, 탐색, 트리, DFS
# 19542번 : 전단지 돌리기

import sys
sys.setrecursionlimit(10 ** 6)


##* DFS 메서드 정의
def dfs(graph, v, visited):
    ##* 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    ##* 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


if __name__ == '__main__':
    N, S, D = map(int, sys.stdin.readline.split())
    graph = {i: [] for i in range(1, N+1)}
    visited = [0] * (N+1)
    ans = 0

    for _ in range(N-1):
        x, y = map(int, sys.stdin.readline.split())
        graph[x] += [y]
        graph[y] += [x]
    dfs()

##! sys.setrecursionlimit()  : 재귀 최대 깊이 설정
##* 재귀 써야하는 경우 필수??
##* 파이썬 기본 재귀 깊이 제한이 1000으로 얕은 편임. 코테풀다가 이제한에 걸릴경우 에러 메세지 볼수 없는 문제점 해결
##* 재귀함수의 깊이를 크게 잡아줌
