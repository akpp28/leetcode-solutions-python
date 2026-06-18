from pprint import pprint
from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return [list(row) for row in zip(*matrix)]



if __name__ == '__main__':
    matrix = [
        [25, 55, 10, 15],
        [50, 10, 20, 30],
        [75, 15, 30, 45],
    ]
    expect = [
        [25, 50, 75],
        [55, 10, 15],
        [10, 20, 30],
        [15, 30, 45],
    ]

    result = Solution().transpose(matrix=matrix)
    pprint(matrix, width=20)
    print('')
    pprint(result, width=20)

    assert expect == result, "Incorrect result"

