# for adjacency matrix to represent graph
# for adjacency matrix to represent graph
G = [[0, 4, 0, 5, 2],
     [4, 0, 1, 2, 0],
     [0, 1, 0, 8, 0],
     [5, 3, 8, 0, 2],
     [2, 0, 0, 2, 0]]
'''for i in range(5):
    for j in range(5):
        if G[i][j]==0:
            G[i][j]=9999
print(G)'''
unvisited={1,2,3,4}
visited={0}
ne=0
mincost=0
while(ne<4):
     min=9999
     x=0
     y=0
     for i in range(5):
      if i in visited:
       for j in range(5):
            if j in unvisited and G[i][j]:
                 if G[i][j] < min:
                    min=G[i][j]
                    x=i
                    y=j
     print(f"{x}-{y}={G[x][y]}")
     mincost+=G[x][y]
     visited.add(y)
     unvisited.discard(y)
     ne+=1
print(mincost)
                    