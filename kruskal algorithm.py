def find(graph,node):
    if graph[node]<0:
        return node
    else:
        temp=find(graph,graph[node])
        graph[node]=temp
        return temp
def union(graph,a,b,d,ans):
    ta=a
    tb=b
    dist=d
    a=find(graph,a)
    b=find(graph,b)
    if a==b:
        pass
    else:
        ans.append([ta,tb,dist])
        if graph[a] < graph[b]: # here graph[a] is more negative value than graph[b]
                     graph[a]+=graph[b]
                     graph[b]=a
        elif graph[a]>graph[b]:
             graph[b]+=graph[a]
             graph[a]=b
        else:#graph[a]=graph[b]
             graph[b]+=graph[a]
             graph[a]=b

#[vertex1,vertex2,weight]
inp=[[1,2,1],[3,4,1],[3,6,2],[6,7,2],[1,3,3],[2,6,4],[4,5,5],[6,5,6],[7,5,7]]
inp.sort(key=lambda x:x[2])
#print(inp)
n=7
graph=[-1]*(n+1)#0,1,2,3,4,5,6,7 here 0 no required
answer=[]
for u,v,d in inp:
    union(graph,u,v,d,answer)
for i in answer:
    print(i)
print('total min distance is ',sum(answer[2]))
print(graph)