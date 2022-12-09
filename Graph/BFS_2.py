graph = {1: set([3, 4]),
         2: set([3, 4, 5]),
         3: set([1, 5]),
         4: set([1]),
         5: set([2, 6]),
         6: set([3, 5])}

from collections import deque

def bfs(graph, root):
    visited = set()
    print('first visited', visited)
    q = deque([root])
    
    while q:
        v = q.popleft()
        print(v, end=' ')
        
        if v not in visited:
            visited.add(v)
            print('visited', visited)
            q += graph[v] - set(visited)
            print('q:', q)
            
    return visited

bfs(graph, 1)