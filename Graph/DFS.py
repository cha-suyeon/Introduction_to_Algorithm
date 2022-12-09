graph1 = {1: set([3, 4]),
         2: set([3, 4, 5]),
         3: set([1, 5]),
         4: set([1]),
         5: set([2, 6]),
         6: set([3, 5])}

graph2 = {0: [1, 2, 3], 1: [0, 2], 2: [0, 1, 4], 3: [0], 4: [2]}

visited = [False] * (len(graph1) + 1)

def dfs(graph, v): # v: 시작 node / root
    
    visited[v] = True
    print(v, end=' ')
    
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i)
            
dfs(graph1, 2)