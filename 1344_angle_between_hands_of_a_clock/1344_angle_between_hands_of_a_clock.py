
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        if hour == 12:
            hour = 0
        min_angle = minutes * 6
        hour_angle = hour * 30 + min_angle / 12
        arbitrary_angle = abs(min_angle - hour_angle)
        return min(arbitrary_angle, 360 - arbitrary_angle)





if __name__ == '__main__':
    # result = Solution().angleClock(hour = 12, minutes = 30)
    # assert result == 165, f"Incorrect value: {result} != 165"
    result = Solution().angleClock(hour = 1, minutes = 57)
    assert result == 76.50000, f"Incorrect value: {result} != 76.50000"
    print(1)