class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1

        #first find proper row
        while l <= r:
            m = l + (r - l) // 2
            print(f"Matrix: {matrix[m][0]}")
            if matrix[m][0] == target:
                return True
            elif matrix[m][0] > target:
                r = m - 1
            else:
                l = m + 1

        if matrix[m][0] > target:
            m -= 1
        row = m
        l = 0
        r = len(matrix[0]) - 1
        while l <= r:
            m = l + (r - l) // 2
            print(f"Matrix: {matrix[row][m]}")
            if matrix[row][m] == target:
                return True
            elif matrix[row][m] > target:
                r = m - 1
            else:
                l = m + 1

        return False

        