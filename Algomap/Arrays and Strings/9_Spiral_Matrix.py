class Solution(object):
    def spiralOrder(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        # Traversed rows/columns
        rightLimit = n
        downLimit = m
        leftLimit = -1
        upLimit = -1

        # Direction states
        right = 0
        down = 1
        left = 2
        up = 3

        # Current direction of movement
        directions = [[0,1], [1,0], [0,-1], [-1,0]]
        direction = right

        # Result
        result = []

        row = 0
        col = 0
        
        while rightLimit - 1 != leftLimit and downLimit - 1 != upLimit:   
            result.append(matrix[row][col])
            
            row += directions[direction][0]
            col += directions[direction][1]

            if col >= rightLimit:
                # col is beyond rightLimit, so move it back in bounds
                col -= 1
                # Current item has already been appended to list, move on to next row
                row += 1
                # If we reached rightLimit, then we just traversed the upper subarray
                upLimit += 1
                # In a spiral, the direction after right is down
                direction = down
            elif row >= downLimit:
                row -= 1
                col -= 1
                rightLimit -= 1
                direction = left
            elif col <= leftLimit:
                col += 1
                row -= 1
                downLimit -= 1
                direction = up
            elif row <= upLimit:
                row += 1
                col += 1
                leftLimit += 1
                direction = right
                 
        return result
