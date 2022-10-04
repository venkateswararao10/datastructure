'''
1. Write an efficient algorithm that searches for a value target in an m * n integer matrix. The matrix has the following properties:
Integers in each row are sorted from left to right
The first integer of each row is greater than the last integer of the previous row.
(Amazon, Facebook, Microsoft, Bloomberg, Uber, Google, Apple)
Example :

	1	3	5	7	
	10	11	15	17
	22	29	32	45

Input: 	matrix = [[1,3,5,7], [10,11,15,17],[22,29,32,45]]
	target = 3
Output: true
'''

#ans:
# 1st approach is iterative approach
'''def search2dmatrix(matrix, target): 
    m, n = len(matrix), len(matrix[0])
    i=0
    j=(m*n)-1
    while(j>=i):
        mid=i+(j-i)//2
        midelement=matrix[mid//n][mid%n] # mid//n is the number of row and mid%n is the number of column
        if(midelement==target):
           return True
        elif target>midelement:
            i=mid+1
        else:
            j=mid-1
    return False
matrix = [[1,3,5,7], [10,11,15,17], [22,29,32,45]]
target = 3
result=search2dmatrix(matrix, target)
print(result)'''

#2nd is recursive approach

def search2dmatrix(matrix, target,i,j): 
    global m
    global n
    
    if i>j:
        return False
    else:
        mid=i+(j-i)//2
        midelement=matrix[mid//n][mid%n] # mid//n is the number of row and mid%n is the number of column
        if(midelement==target):
           return True
        elif target>midelement:
           return search2dmatrix(matrix, target,mid+1,j)
        else:
           return search2dmatrix(matrix, target,i,mid-1)
    
matrix = [[1,3,5,7], [10,11,15,17], [22,29,32,45]]
target = 3
m, n = len(matrix), len(matrix[0])
i=0
j=(m*n)-1
result=search2dmatrix(matrix, target,i,j)
print(result)