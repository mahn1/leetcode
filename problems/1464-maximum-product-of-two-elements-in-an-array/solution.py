from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Все nums[i] >= 1, значит множители (nums[i] - 1) >= 0:
        # произведение максимально на двух наибольших элементах.
        first = second = 0  # first >= second
        for v in nums:
            if v > first:
                first, second = v, first
            elif v > second:
                second = v
        return (first - 1) * (second - 1)


if __name__ == "__main__":
    import random

    s = Solution()
    assert s.maxProduct([3, 4, 5, 2]) == 12
    assert s.maxProduct([1, 5, 4, 5]) == 16
    assert s.maxProduct([3, 7]) == 12
    assert s.maxProduct([1, 1]) == 0
    for _ in range(500):
        a = [random.randint(1, 20) for _ in range(random.randint(2, 8))]
        expected = max((a[i] - 1) * (a[j] - 1) for i in range(len(a)) for j in range(i + 1, len(a)))
        assert s.maxProduct(a) == expected, a
    print("OK")
