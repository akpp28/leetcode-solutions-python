"""
https://www.youtube.com/watch?v=6X7Ha2PrDmM


"""
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # dynamic programming: bottom up
        # recursive: top down
        if not matrix:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        cache: dict[tuple[int, int], int] = {}  # map each (r, c) -> max length of square
        matrix_stub= [[0]* cols for _  in range(rows)]

        # T: O(m*n) M: O(m*n)
        def helper(r, c):
            if r >= rows or c >= cols:
                return 0

            if (r, c) not in cache:
                down = helper(r + 1, c)
                right = helper(r, c + 1)
                diag = helper(r + 1, c + 1)
                cache[(r,c)] = 0
                if matrix[r][c] == "1":
                    cache[(r,c)] = 1 + min(down, right, diag)

            return cache[(r, c)]
        helper(0, 0)

        # for r in range(rows):
        #     for c in range(cols):
        #         matrix_stub[r][c] = cache[(r, c)]
        # print(matrix_stub)
        return max(cache.values()) ** 2


if __name__ == '__main__':
    # result = Solution().maximalSquare(matrix=[
    #     ["1", "1", "1", "0"],
    #     ["1", "1", "1", "1"],
    #     ["0", "1", "1", "1"],
    #     ["0", "1", "1", "1"]
    # ])
    #
    # dp1 = [
    #     [1, 1, 1, 0],
    #     [1, 2, 2, 1],
    #     [0, 1, 2, 2],
    #     [0, 1, 2, 3]
    # ]
    #
    # print(f'result: {result}')

    # result = Solution().maximalSquare(matrix=[["0"]])
    # print(f'result: {result}')
    result = Solution().maximalSquare(matrix=[
        ["1", "0", "1", "1"],
        ["1", "1", "0", "1"],
        ["1", "1", "1", "1"],
    ])

    dp = [
        [1, 0, 1, 1],
        [2, 1, 0, 1],
        [1, 1, 1, 1]
    ]

    print(f'result: {result}')
