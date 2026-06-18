
"""
https://www.youtube.com/watch?v=6X7Ha2PrDmM

"""
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]
        max_side = 0

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1  # first row/col can only be 1×1
                    else:
                        dp[i][j] = min(dp[i - 1][j],  # top
                                       dp[i][j - 1],  # left
                                       dp[i - 1][j - 1]  # diagonal
                                       ) + 1
                    max_side = max(max_side, dp[i][j])

        print(dp)
        return max_side * max_side  # area = side²


if __name__ == '__main__':
    result = Solution().maximalSquare(matrix=[
        ["1", "1", "1", "0"],
        ["1", "1", "1", "1"],
        ["0", "1", "1", "1"],
        ["0", "1", "1", "1"]
    ])

    dp1 = [
        [1, 1, 1, 0],
        [1, 2, 2, 1],
        [0, 1, 2, 2],
        [0, 1, 2, 3]
    ]

    print(f'result: {result}')

    # result = Solution().maximalSquare(matrix=[["0"]])
    # print(f'result: {result}')
