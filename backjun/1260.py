# DFS와 BFS

N, M, V = map(int, input().split())

# Matrix
graph = [[0]*(N+1) for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1
    
visited1 = [0]*(N+1)
visited2 = visited1.copy()

def dfs(V):
    visited1[V] = 1 # 방문처리
    print(V, end=' ')
    for i in range(1, N+1):
        if graph[V][i] == 1 and visited1[i] == 0:
            dfs(i)

