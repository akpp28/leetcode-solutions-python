from pprint import pprint
from typing import List



class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])
        tmp = [[0] * rows for _ in range(cols)]

        for r in range(rows):
            for c in range(cols):
                tmp[c][r] = matrix[r][c]
        return tmp



if __name__ == '__main__':
    matrix = [
        [25, 55, 10, 15],
        [50, 10, 20, 30],
        [75, 15, 30, 45],
    ]
    result = Solution().transpose(matrix=matrix)
    pprint(matrix, width=20)
    print('')
    pprint(result, width=20)