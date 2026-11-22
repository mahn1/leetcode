from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # seen[значение] = индекс, на котором оно уже встречалось.
        seen = {}
        for i, num in enumerate(nums):
            need = target - num
            if need in seen:
                return [seen[need], i]
            # Кладём число после проверки: пара из двух одинаковых
            # (nums = [3, 3], target = 6) не схватит один и тот же индекс.
            seen[num] = i
        return []


if __name__ == "__main__":
    s = Solution()
    assert s.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert s.twoSum([3, 2, 4], 6) == [1, 2]
    assert s.twoSum([3, 3], 6) == [0, 1]
    assert s.twoSum([-1, -2, -3, -4, -5], -8) == [2, 4]
    assert s.twoSum([0, 4, 3, 0], 0) == [0, 3]
    print("OK")
