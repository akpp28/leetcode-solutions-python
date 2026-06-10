import json
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        max_side_length = 0
        matrix = [[int(item) for item in row] for row in matrix] # convert all values to integers

        for x in range(rows):
            for y in range(cols):
                if matrix[x][y] == 0:
                    continue

                max_possible_side_length = min(rows - x, cols - y)
                for size in range(1, max_possible_side_length + 1):
                    # The "Outer Shell": right wall (X-axis) then bottom floor (Y-axis)
                    right_wall_ok = all(matrix[next_x][y + size - 1] for next_x in range(x, x + size))
                    bottom_floor_ok = all(matrix[x + size - 1][next_y] for next_y in range(y, y + size))

                    if not right_wall_ok or not bottom_floor_ok:
                        break

                    max_side_length = max(max_side_length, size)

        # Return the final area (side * side)
        return max_side_length * max_side_length


if __name__ == '__main__':
    result = Solution().maximalSquare(matrix=[
        ["1","1","0","1"],
        ["1","1","0","1"],
        ["1","1","1","1"]
    ])
    print(f'result: {result}')
