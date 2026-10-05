class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        upto = len(matrix) // 2
        l = len(matrix)
        x=0
        while x < upto:
            temp = matrix[x]
            matrix[x] = matrix[l - x - 1]
            matrix[l - x - 1] = temp
            x += 1
        
        print(matrix)

        i = 0
        while i < l:
            j = i + 1
            while j < l:
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                j += 1
            i += 1
        
        # return matrix