# DFS와 BFS
from collections import deque

# 정점의 개수 N, 간선의 개수 M, 탐색을 시작할 정점의 번호 V
N, M, V = map(int, input().split())

# Matrix
graph = [[0]*(N+1) for _ in range(N+1)]
# print(graph)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1
    
visited = [0]*(N+1)

def dfs(V):
    visited[V] = 1 # 방문처리
    print(V, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in range(1, N+1):
        if graph[V][i] == 1 and visited[i] == 0:
            dfs(i)

def bfs(V):
    q = deque()
    q.append(V)
    visited[V] = 1 # 방문처리
    while q: # queue가 빌 때까지 반복
        V = q.popleft() # queue에서 하나의 원소를 뽑아 출력
        print(V, end=' ')
        # 아직 방문하지 않은 인접한 원소들을 queue에 삽입
        for i in range(1, N+1):
            if graph[V][i] and visited[i] == 0:
                q.append(i)
                visited[i] = 1

dfs(V)
print()
bfs(V)
