graph1 = {1: set([3, 4]),
         2: set([3, 4, 5]),
         3: set([1, 5]),
         4: set([1]),
         5: set([2, 6]),
         6: set([3, 5])}

graph2 = {0: [1, 2, 3], 1: [0, 2], 2: [0, 1, 4], 3: [0], 4: [2]}

# visited = [False] * (len(graph2) + 1)
# print(visited)

from collections import deque

def bfs(graph, root):
    q = deque([root])
    visited = [False] * (len(graph) + 1)
    visited[root] = True
    
    while q:
        v = q.popleft()
        print(v, end=' ')
        
        for i in graph[v]:
            # print("i:", i)
            if not visited[i]:
                q.append(i)
                visited[i] = True
                # print(visited)

# bfs(graph1, 1)
bfs(graph2, 0)