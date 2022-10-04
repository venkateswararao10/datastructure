'''Write an efficient algorithm that searches for a value target in an m * n integer matrix. The matrix has the following properties:
Integers in each row are sorted in ascending order from left to right.
Integers in each column are sorted in ascending order from top to bottom.
(Amazon, Microsoft, Facebook, Bloomberg, Apple, Oracle)
Example:
	1	4	7	11	15	
	2	5	8	12	19
	3	6	9	16	22
	10	13	14	17	24
	18	21	23	28	30
Input:   matrix=[[1,4,7,11,15], [2,5,8,12,19],[3,6,9,16,22][10,13,14,17,24][18,21,23,28,30]]
	target=5
Output: true
'''

#code:
def searchelematrix(matrix, target):
	noofcols=len(matrix[0])
	noofrows=len(matrix)
	rowno=noofrows-1
	colno=0
	while colno<noofcols and rowno>=0:
		if matrix[rowno][colno]<target:
			colno+=1
		elif matrix[rowno][colno]>target:
                 rowno-=1
		else:
			return True
	return False


matrix=[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,28,30]]
target=5
result=searchelematrix(matrix, target)
print(result)
