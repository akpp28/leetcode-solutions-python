"""
https://leetcode.com/problems/last-stone-weight-ii/description/

1049. Last Stone Weight II, Medium

You are given an array of integers stones where stones[i] is the weight of the ith stone.
We are playing a game with the stones. On each turn, we choose any two stones and smash them together. Suppose the stones have weights x and y with x <= y. The result of this smash is:
If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the __smallest possible weight__!!! of the left stone. If there are no stones left, return 0.

Own hints:
1. Knapsack Problem (задача про рюкзак)
2. Subset Sum Problem (задача про суму підмножини)
  Чому Last Stone Weight II зводиться до Subset Sum?
  https://chatgpt.com/c/6a1b63f4-b5a0-83eb-b283-6525c1885055


stones = [2,7,4,1,8,1]

stone 2: {0, 2}
stone 7: {0, 9, 2, 7}
stone 4: {0, 2, 4, 6, 7, 9, 11, 13}
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22}
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23}

related:
* 2035. Partition Array Into Two Arrays to Minimize Sum Difference
"""
from typing import List


# readable solution
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total_stones_sum = sum(stones)  # 23
        possible_sums = {0}

        for stone in stones:
            next_ps = set()
            for ps in possible_sums:
                next_ps.add(ps) # don't take stone
                next_ps.add(ps + stone) # take stone
            possible_sums = next_ps

        best = max(s for s in possible_sums if s <= total_stones_sum // 2)
        group1 = best
        group2 = total_stones_sum - best

        return abs(group2 - group1)


if __name__ == '__main__':
    result = Solution().lastStoneWeightII(stones=[2, 7, 4, 1, 8, 1])
    print(f"result: {result}")
