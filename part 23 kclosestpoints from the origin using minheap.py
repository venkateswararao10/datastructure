from heapq import heappush, heappop
import math

## Method definition to get kclosestpoints from the origin using minheap approach
def kClosestPoints(points, k):
    ## to get the  distance from the origin to given point
    def get_distance(x, y):
        return math.sqrt(x ** 2 + y ** 2)
    
    min_heap = []
    n = len(points)

    ## to traverse all the points
    for i in range(n):
        x = points[i][0]
        y = points[i][1]
        ## inserting the distance and the points inside a minheap
        heappush(min_heap, (get_distance(x,y), points[i]))
    
    result = []
    ## to pop the k values from minheap to extract the k closest points inside the result list
    for i in range(k):
        result.append(heappop(min_heap) [1])

    return result

## Driver code
points = [[2, -1], [3, 2], [4, 1], [-1, -1], [-2, 2]]
k = 3
result = kClosestPoints(points, k)
print("Closest points to the origin are:", result)
