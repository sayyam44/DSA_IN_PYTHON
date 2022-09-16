# https://leetcode.com/problems/rotate-image/discuss/842087/Easy-Python-from-scratch-(2-Steps)
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]

def rotate(matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        #brute force--tc=n2,sc=n2
        #use another empty matrix and directly change the rows with columns
        
        #optimized sol---reverse the matrix on rows and then find transpose(change all rows with columns) of the matrix 
        #tc=n2+n2=n2 --- to transpose and reverse the matrix
        #sc=1 (as no extra matrix is being used)
        
        #step1-making 1st row as last row and similarly other rows.
    
        l = 0
        r = len(matrix) -1
        while l < r:
            matrix[l], matrix[r] = matrix[r], matrix[l]
            l += 1
            r -= 1
        #  reversing all columns
        # matrix_1 = [['c1', 'c2', 'c3'],
        #     [10, 20, 30],
        #     [40, 50, 60],
        #     [70, 80, 90]]
 
        # creating an empty array to store the reversed column matrix
        # matrix_2 = []
        
        # looping through matrix_1 and appending matrix_2
        # for i in range(len(matrix_1)):
        #     matrix_2.append(matrix_1[i][::-1])
            
        #step2-transposing the matrix
        for i in range(len(matrix)): 
            for j in range(i):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    
        return matrix