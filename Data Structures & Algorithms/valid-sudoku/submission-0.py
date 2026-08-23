class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board[0])):
            #will happen 9 times
            grid = set()
            for c in range(len(board)):
                currentNum = board[i][c]
                if currentNum != '.':
                    if currentNum not in grid:
                        grid.add(currentNum)
                    else:
                        return False
                #will happen 81 times

        for i in range(len(board[0])):
            #will happen 9 times
            print(f"{grid}")
            grid = set()
            print("New Col")
            for c in range(len(board)):
                currentNum = board[c][i]
                if currentNum != '.':
                    print(f"{currentNum}")
                    if currentNum not in grid:
                        grid.add(currentNum)
                    else:
                        print(f"current Num: {currentNum} already in grid c: {c} i: {i}")
                        return False
                #will happen 81 times

        #find a way for the 3x3 to be done
        for x_offset in range(3):
            x = 3 * x_offset
            for y_offset in range(3):
                y = 3 * y_offset
                print(f"{grid}")
                grid = set()
                print("New 3x3")
                for i in range(3):
                    for c in range(3):
                        currentNum = board[i + x][c + y]
                        if currentNum != '.':
                            print(f"{currentNum}")
                            if currentNum not in grid:
                                grid.add(currentNum)
                            else:
                                print(f"current Num: {currentNum} already in grid c: {c} i: {i}")
                                print(grid)
                                return False

                    
                    

        return True


        