## Time complexity:O(n^2 logn)

from heapq import heappush, heappop
## Method definition to get kth smallest element in 2D matrix using minheap approach
def ksmallestElement(matrix, k):
    n_rows = len(matrix)
    n_cols = len(matrix[0])
    
    min_heap = []

    ## traverse the elements inside the matrix
    for i in range(n_rows):
        for j in range(n_cols):
            ## insertion in a minheap
            heappush(min_heap, matrix[i][j])
        
    ## pop k number of times to get kth smallest element from min_heap
    for i in range(k):
        result = heappop(min_heap)
    
    return result

## Driver code
matrix=[[1, 4, 7], [3, 5, 9], [6, 8, 11]]
k = 4
result = ksmallestElement(matrix, k)
print("Kth smallest element in 2D Matrix is:", result)
