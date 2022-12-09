graph1 = {1: set([3, 4]),
         2: set([3, 4, 5]),
         3: set([1, 5]),
         4: set([1]),
         5: set([2, 6]),
         6: set([3, 5])}

graph2 = {0: [1, 2, 3], 1: [0, 2], 2: [0, 1, 4], 3: [0], 4: [2]}

def dfs(graph, v, visited = None): # v: 시작 node / root
    if visited is None:
        visited = set()
    visited.add(v)
    
    print(v, end=' ')
    
    for i in graph[v] - visited:
        dfs(graph, i, visited)
        
    return visited
            
dfs(graph1, 2)