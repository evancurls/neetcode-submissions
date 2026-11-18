class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l,r = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l):
                top, bottom = l,r
                t_l = matrix[top][l + i]

                #assign top left
                matrix[top][l + i] = matrix[bottom - i][l]
                #assign bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]
                #assign bottom right
                matrix[bottom][r - i] = matrix[top + i][r]
                #assign top right
                matrix[top + i][r] = t_l 
            l += 1
            r -= 1
