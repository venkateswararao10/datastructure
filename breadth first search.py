
queue=[]
def breadth_first_traversal(visited,graph,node):
    visited.add(node)
    queue.append(node)
    while queue:
        x=queue.pop(0)
        print(x)
        for i in graph[x]:
            if i not in visited:
                visited.add(i)
                queue.append(i)
# visited set to keep track of all the visited nodes
visited = set()

## driver code
graph = {
    'A' : ['B', 'C', 'D'],
    'B' : ['E'],
    'C' : ['E', 'F'],
    'D' : ['F'],
    'E' : ['G'],
    'F' : ['G'],
    'G' : []
}

breadth_first_traversal(visited, graph, 'A')